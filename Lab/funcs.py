import numpy as np
import pandas as pd
from scipy.optimize import fsolve
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks, hilbert

def dispersion_relation(k, H):
    g = 9.81
    return  g*k*np.tanh(k*H)

def dispersion_relation_derivative_k(k, H):
    g = 9.81
    tanh_kH = np.tanh(k*H)
    sech_kH = 1 / np.cosh(k*H)
    return g*tanh_kH + g*k*H*sech_kH**2

def solve_disp_for_H(freq, lamb):
    g = 9.81
    k = (2*np.pi)/lamb
    omega = 2*np.pi*freq
    R = (omega**2)/(g*k)
    H_eff = np.arctanh(R)/k

    return H_eff

def cut_transient_fronts(df, cut_times):
    """
    Cut off transient fronts at each probe based on cut_times.
    Assumes that the dataframe has a 'time' column.
    """
    r_cut = df.copy()

    for i, col in enumerate(df.columns[1:5]):
        cut_time = cut_times[i]
        r_cut[col] = df.loc[df['time'] >= cut_time, col]

    return r_cut


def estimate_wavenumber(freq, depth, g=9.81, tol=1e-10, max_iter=100):
    """
    Estimate the wavenumber k using the dispersion relation for linear waves,
    using the Newton-Raphson iterative method.
    
    Parameters:
    freq : float
        Observed frequency in Hz.
    depth : float
        Water depth in meters.
    """
    omega = 2 * np.pi * freq  # Angular frequency

    # Initial guess for k using deep water approximation
    k_guess = omega**2 / g
    # Modifying initial guess for finite depth
    k_guess = omega**2 / (g * np.tanh(k_guess * depth))

    for i in range(max_iter):
        f = dispersion_relation(k_guess, depth) - omega**2
        df_dk = dispersion_relation_derivative_k(k_guess, depth)
        k_new = k_guess - (f / df_dk)

        if abs(k_new - k_guess) < tol:
            return k_new
        
        k_guess = k_new
    raise ValueError("Wavenumber estimation did not converge")
    


def max_waves_b4_reflection(tank_length,
                            depth,
                            frequency,
                            wavenumber,
                            probe_positions,
                            cut_times):
    """
    Compute maximum number of waves (and effective times) before the first reflected waves reach each probe.

    Parameters
    ----------
    tank_length : float
        Length of the tank (m), wavemaker at x=0, far wall at x=tank_length.
    depth : float
        Water depth H (m).
    frequency : float
        Dominant wave frequency f (Hz).
    wavenumber : float
        Dominant wavenumber k (1/m).
    probe_positions : array_like
        Probe x-positions (m)
    cut_times : array_like
        Time at which the beginning of the signal is cut for each probe (s). To avoid transient fronts.

    Returns
    -------
    max_waves_list : ndarray
        Maximum number of full wave periods usable before reflection contaminates each probe.
    effective_time : ndarray
        Usable time window (s) before reflection: max(0, (2L - x_p)/c_g - cut_time)
    """
    # Wave properties
    omega = 2.0 * np.pi * frequency
    wave_period = 1.0 / frequency
    c = omega / wavenumber  # Phase speed

    # Group speed for linear waves
    cg = (c / 2) * (1 + (2 * wavenumber * depth) / (np.sinh(2 * wavenumber * depth)))
 
    # Reflection arrival time at probe: (2L - x_p)/cg
    reflection_time = (2.0 * tank_length - probe_positions) / cg

    # Effective usable time before reflection
    usable_time = reflection_time - cut_times

    # Avoid negative usable times
    usable_time = np.maximum(usable_time, 0.0)

    # Max number of waves
    max_waves = usable_time / wave_period

    return max_waves, usable_time

def cut_off_reflections(data, frequency, usable_time):
    """
    Cut off data after effective times to avoid reflection contamination.
    Cutting to keep only full wave periods.
    
    Parameters
    ----------
    data : pd.DataFrame
        DataFrame containing time series data from probes.

    frequency : float
        Frequency of the waves in Hz.

    effective_times : ndarray
        Array of effective times for each probe.

    Returns
    -------
    cut_data : pd.DataFrame
        DataFrame with data after effective times set to NaN.
    """
    cut_data = data.copy()
    wave_period = 1 / frequency

    for i, use_time in enumerate(usable_time):
        max_full_periods = int(use_time // wave_period)
        cut_off_time = max_full_periods * wave_period
        # Time after transient front and before reflections
        valid_time = use_time + cut_off_time
        probe_col = f'P_{i}'
        cut_data.loc[cut_data['time'] > valid_time, probe_col] = np.nan

    return cut_data

def cut_out_valid_data(data, frequency, depth, wave_maker_build_up_time, x_probe_pos):
    """
    Cut off invalid data from the DataFrame based on transient front arrival times and reflection arrival times.
    Also trims to ensure integer number of wave periods using zero-crossings.
    """
    print('----- Cutting out invalid data -----')

    # Step 1: Transient front arrival times at each probe
    transient_front_velocity = x_probe_pos[0] / wave_maker_build_up_time  # m/s
    build_up_time = x_probe_pos / transient_front_velocity
    print(f'Time after transient front reaches each probe: {build_up_time}')
    print()

    # Step 2: Reflection arrival times
    omega = 2 * np.pi * frequency
    k = estimate_wavenumber(frequency, depth)
    c = omega / k
    cg = 0.5 * c * (1 + (2 * k * depth) / np.sinh(2 * k * depth))

    tank_length = 25.0
    reflection_distances = 2 * (tank_length - x_probe_pos)
    reflection_times = reflection_distances / cg

    print(f'Reflection arrival times at each probe: {reflection_times}')
    print()
    print(f'Time window between build-up and reflection at each probe: {reflection_times - build_up_time}')
    print()
    print(f'Maximum number of usable wave periods at each probe: {(reflection_times - build_up_time) * frequency}')
    print('-------------------------------------------------')

    # Step 3: Keep only valid window (between build-up and reflection)
    valid = data.copy()
    probe_cols = valid.columns[1:5]

    for i, col in enumerate(probe_cols):
        mask = (valid["time"] < build_up_time[i]) | (valid["time"] > reflection_times[i])
        valid.loc[mask, col] = np.nan

    # Step 4: Zero-crossing trimming (ensure integer number of wave periods)

    for col in probe_cols:
        series = valid[col]

        # Keep only valid, not nans
        y = series.dropna()

        # Upward zero crossings: y[t-1] < 0 AND y[t] >= 0
        y_shift = y.shift(1)
        upward_crossings = y.index[(y_shift < 0) & (y >= 0)]

        # Need at least 2 crossings for at least one full period
        if len(upward_crossings) < 2:
            continue

        start_idx = upward_crossings[0]
        end_idx = upward_crossings[-1]

        # Cut everything before start and after end
        series.loc[:start_idx] = np.nan
        series.loc[end_idx+1:] = np.nan

        valid[col] = series

    return valid