import numpy as np
import pandas as pd
from scipy.optimize import fsolve
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks, hilbert

def dispersion_relation(k, H):
    g = 9.81
    return  g*k*np.tanh(k*H)

def solve_disp_for_H(freq, lamb):
    g = 9.81
    k = (2*np.pi)/lamb
    omega = 2*np.pi*freq
    R = (omega**2)/(g*k)
    H_eff = np.arctanh(R)/k

    return H_eff

def phase_speed(wavelength, frequency):
    wave_number = 2 * np.pi / wavelength
    angular_frequency = 2 * np.pi * frequency
    c = angular_frequency / wave_number
    return c

def frequency_analysis(r_cut):
    
    signals = [[],[],[],[]]  # for storing probe signals

    for i in range(1, 5):
        signals[i-1] = r_cut.iloc[:, i].values
    
    signals = np.array(signals)

    sample_rate = 250  # Samples per second
    n = len(r_cut)  # Number of samples
    dt = 1 / sample_rate  # Time between samples

    fft_signals = fft(signals, axis=1)
    freqs = fftfreq(n, d=dt)

    # Keep only positive frequencies
    pos_freqs = freqs[:n//2]
    fft_pos = fft_signals[:, :n//2]

    # Find the dominant frequency, here done at the first probe
    power = np.abs(fft_pos[0])**2
    dominant_idx = np.argmax(power[1:]) + 1 # skip the zero frequency
    f_dom = pos_freqs[dominant_idx]

    return f_dom


def estimate_wavenumber(f_obs, depth):
    """
    Estimate the wavenumber k using the dispersion relation for linear waves.
    
    Parameters:
    f_obs : float
        Observed frequency in Hz.
    depth : float
        Water depth in meters.
    """
    g = 9.81  # Acceleration due to gravity in m/s^2
    omega = 2 * np.pi * f_obs  # Angular frequency

    # Initial guess for k using deep water approximation
    k_guess = omega**2 / g

    # Iteratively solve for k using the dispersion relation
    for _ in range(10):
        k_guess = (omega**2) / (g * np.tanh(k_guess * depth))

    return k_guess

def max_waves_b4_reflection(tank_length, depth, frequency, wavelength, probe_positions, wave_maker_build_up_time):
    """
    Calculate the maximum number of waves before reflections affect measurements at each probe.

    Parameters:
    tank_length (float): Length of the wave tank (meters).
    depth (float): Depth of the water in the tank (meters).
    frequency (float): Frequency of the wave (Hz).
    wavelength (float): Wavelength of the wave (meters).
    probe_positions (list or array): List of x-positions of the probes along the tank (meters).

    Returns:
    list: Maximum number of waves before reflections at each probe.
    """
    # Calculate wave properties
    wave_num = 2 * np.pi / wavelength  # Wave number k
    omega = np.sqrt(dispersion_relation(wave_num, depth))  # Angular frequency
    phase_speed = omega / wave_num  # Phase speed 
    wave_period = 1 / frequency  # Wave period

    max_waves_list = []

    for probe_pos in probe_positions:
        # Distance from probe to far end of the tank
        distance_to_far_end = tank_length - probe_pos

        # Round-trip time for reflections to return to the probe
        round_trip_time = 2 * distance_to_far_end / phase_speed

        # Effective time available for generating waves
        effective_time = round_trip_time - wave_maker_build_up_time

        # Handle cases where reflections return before the wave train stabilizes
        if effective_time < 0:
            max_waves = 0  # No valid waves before reflections
        else:
            # Maximum number of waves before reflections return
            max_waves = effective_time / wave_period

        max_waves_list.append(max_waves)

    return max_waves_list
