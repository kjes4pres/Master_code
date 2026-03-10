import numpy as np
import pandas as pd
from scipy import stats
from scipy.signal import find_peaks

def get_amp_n_err_lists(df):
    """
    Find the observed amplitude and standard error at each probe.
    """
    std_list = np.array([df['P_0'].std(), df['P_1'].std(), df['P_2'].std(), df['P_3'].std()])
    amp_list = std_list * np.sqrt(2)

    # Number of data points per probe
    n_0 = df["P_0"].count()
    n_1 = df["P_1"].count()
    n_2 = df["P_2"].count()
    n_3 = df["P_3"].count()
    len_list = np.array([n_0, n_1, n_2, n_3])
    
    err_list = std_list / np.sqrt(len_list)

    return amp_list, err_list


def get_obs_damping_coeff(amp_list, probe_pos, ci=0.05):
    """
    Find the observed spatial damping coefficient by fitting
    ln(A) = ln(A0) - alpha * x.

    Returns (alpha, se_alpha).
    """
    amp = np.asarray(amp_list)
    x = np.asarray(probe_pos)

    y = np.log(amp)

    # linear fit y = b + m*x
    (m, b), cov = np.polyfit(x, y, 1, cov=True)

    alpha = -m
    # standard error of slope is sqrt(cov[0,0])
    se_alpha = np.sqrt(cov[0, 0])

    n = len(x)
    dof = n - 2  # degrees of freedom
    t_val = stats.t.ppf(1 - ci/2, dof)

    return alpha, se_alpha, t_val

# ----------------------------------------------------------
# Analytical functions
# and functions from Weber's theory

"""
Functions for calculating theoretical values,
for comparison with experimental results.
"""

def vertical_velocity(eta, D, H, f, a, k, h):
    """
    Calculate the average vertical velocity
    at the top of the platess.
    
    Corresponds to the real part of the modified version 
    of Equation 56 in Weber (2025).

    Parameters:
        eta : Wave amplitude (m)
        D : total water depth (m)
        H : depth of plate top (m)
        f : wave frequency (Hz)
        a : spatial damping coefficient (1/m)
        k : wavenumber (1/m)
        h : plate spacing (m)

    Returns:
        w_bar : average vertical velocity (m/s)
    """

    # Constants
    g = 9.81  # gravitational acceleration (m/s^2)
    nu = 1e-6  # kinematic viscosity of water (m^2/s)

    # Angular frequency
    omega = 2 * np.pi * f

    nominator = g*eta*(D - H) * (2*omega*a*k - (12*nu*(k**2 + a**2)/h**2))
    denominator = (12*nu/h**2)**2 + omega**2

    w_bar = nominator / denominator

    return w_bar

def full_w_vel(w, dw, R):
    '''
    Get the imaginary part of the vertical velocity at the top of the plates,
    using the Robin boundary condition.
    '''
    w_i = -R*dw
    dw_i = w/R
    return w_i, dw_i

def theoretical_omega(k, H, D, a, h):
    """
    Calculate the theoretical angular frequency.
    Corresponds to the modified version of Equation 58 in Weber (2025).

    Parameters:
        k : wavenumber (1/m)
        H : depth of plate top (m)
        D : total water depth (m)
        a : spatial damping coefficient (1/m)
        h: plate spacing (m)

    Returns:
        omega : theoretical angular frequency (rad/s)
    """

    # Constants
    g = 9.81  # gravitational acceleration (m/s^2)
    nu = 1e-6  # kinematic viscosity of water (m^2/s)

    omega = k*np.sqrt(g*H) + (g*D*a*k*h**2)/(12*nu)

    return omega


def spatial_damping_coefficient(k, D, H, h = 0.01):
    """
    Calculate the theoretical spatial damping coefficient.
    Corresponds to the modified version of Equation 59 in Weber (2025).

    Parameters:
        k : wavenumber (1/m)
        h : plate spacing (m)
        D : total water depth (m)
        H : depth of plate top (m)

    Returns:
        alpha : spatial damping coefficient (1/m)
    """

    # Constants
    g = 9.81  # gravitational acceleration (m/s^2)
    nu = 1e-6  # kinematic viscosity of water (m^2/s)

    omega_0 = k*np.sqrt(g*H)
    alpha_weber = k*h**2*omega_0*(D - H)/(24*H*nu)

    Q = (3 - D/H)*g*D*h**4*k**2 / (288*nu**2)

    alpha = alpha_weber / (1 + Q)
    
    return alpha


def robin_parameter(H, a, k):
    """
    Calculate the Robin boundary condition parameter R.
    Corresponds to the modified version of Equation 60 in Weber (2025).

    Parameters:
        H : depth of plate top (m)
        a : spatial damping coefficient (1/m)
        k : wavenumber (1/m)

    Returns:
        R : Robin parameter (???)
    """
    R = (2*H*a)/(k)

    return R

def get_amplitudes_from_run(y, use_minima=True, distance=10):
    """
    y: time series from one probe
    use_minima: if True, include troughs as well as crests
    distance: minimum distance between peaks (in samples)
    Returns: 1D numpy array of amplitudes (peak values)
    """
    y = np.asarray(y)

    # Maxima
    peaks_max, _ = find_peaks(y, distance=distance)
    amps_max = y[peaks_max]

    if not use_minima:
        return amps_max

    # Minima
    peaks_min, _ = find_peaks(-y, distance=distance)
    amps_min = y[peaks_min]

    return np.abs(np.concatenate([amps_max, amps_min]))

def amplitude_distributions(runs_amplitudes, n_bins=50):
    
    # Amplitudes from the three runs, concatenated for binning
    all_amps = np.concatenate([np.asarray(a) for a in runs_amplitudes])

    bins = np.linspace(all_amps.min(), all_amps.max(), n_bins + 1)

    hists = []

    for amps in runs_amplitudes:

        amps = np.asarray(amps)
        hist, _ = np.histogram(amps, bins=bins, density=True)
        hists.append(hist)

    hists = np.vstack(hists)                    # shape: (n_runs, n_bins)
    mean_hist = hists.mean(axis=0)
    std_hist = hists.std(axis=0)
    bin_centers = 0.5 * (bins[:-1] + bins[1:])
    
    return bin_centers, hists, mean_hist, std_hist, bins
