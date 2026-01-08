"""
Functions no longer in use but kept here due to emotional attachment.
"""

def interpolate_missing(df):
    '''
    Interpolates missing values in the DataFrame.
    '''
    df_interpolated = df.copy()
    df_interpolated.interpolate(method='linear', inplace=True)
    return df_interpolated


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