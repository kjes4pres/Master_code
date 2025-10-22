from scipy.fft import fft, fftfreq
import numpy as np

def estimate_wavelength(df, probe_positions):
    signals = [[],[],[],[]]  # for storing probe signals

    for i in range(1, 5):
        signals[i-1] = df.iloc[:, i].values
    
    signals = np.array(signals)
    n_probes = 4

    total_time = (df['time'].iloc[-1] - df['time'].iloc[0]).total_seconds()
    dt = total_time / len(df['time'])  # time step
    fs = 1 / dt  # sample frequency
    n = len(df['time'])
    
    # FFT of each signal
    fft_signals = fft(signals, axis=1)
    freqs = fftfreq(n, d=dt)
    
    # Keep only positive frequencies
    pos_freqs = freqs[:n//2]
    fft_pos = fft_signals[:, :n//2]
    
    # Find the dominant frequency (for example, on the signal of the 1st probe)
    power = np.abs(fft_pos[0])**2
    dominant_idx = np.argmax(power[1:]) + 1  # ignore DC (frequency 0)
    f_dom = pos_freqs[dominant_idx]
    omega_dom = 2 * np.pi * f_dom

    # Extract phases at this frequency for each probe
    phases = np.angle(fft_pos[:, dominant_idx])
    unwrapped_phases = np.unwrap(phases)

    # Linear fit: phase = k * x + phi0 → slope = k
    coeffs = np.polyfit(probe_positions, unwrapped_phases, 1)
    
    k = coeffs[0]  # wave number (rad/m)

    # Wavelength
    wavelength = 2 * np.pi / np.abs(k)
    
    return wavelength, f_dom