import numpy as np
import pandas as pd
from scipy import stats
from scipy.signal import find_peaks

def find_positive_peaks(freq, df, col):
    """
    Find positive peaks in a column of a DataFrame based on frequency and sample rate.
    """
    # Expected distance between peaks in samples, based on the frequency and sample rate of 250 Hz
    distance = (1/freq) * 250 * 0.8

    # Allowing amplitudes to be 10% lower than expected from linear theory,
    # and 20% higher, to account for experimental variability and noise.
    lower_bound = 0.9*np.sqrt(2)*np.nanstd(df[col])
    upper_bound = 1.2*np.sqrt(2)*np.nanstd(df[col])

    peak_idx = find_peaks(df[col], height=(lower_bound, upper_bound), distance=distance)[0]

    peaks = df[col].values[peak_idx]
    positive_peaks = peaks[peaks > 0]

    return positive_peaks

def mean_amp_and_err(peaks):
    """
    Calculate the mean amplitude and error from a list of peak values.
    """
    amps = np.array(peaks)
    mean_amp = np.nanmean(amps)
    std_amp = np.nanstd(amps, ddof=1)  # sample standard deviation
    n = len(amps)
    err_amp = std_amp / np.sqrt(n)
    return mean_amp, err_amp

def get_obs_damping_coeff(amps, probe_pos):
    """
    Find the observed spatial damping coefficient by fitting
    ln(A) = ln(A0) - alpha * x.

    Returns (alpha, se_alpha).
    """
    amp = np.asarray(amps)
    x = np.asarray(probe_pos)

    y = np.log(amp)

    # linear fit y = b + m*x
    (m, b), cov = np.polyfit(x, y, 1, cov=True)

    alpha = -m
    # standard error of slope is sqrt(cov[0,0])
    se_alpha = np.sqrt(cov[0, 0])

    return alpha, se_alpha

# ----------------------------------------------------------
# Analytical functions
# and functions from Weber's theory

"""
Functions for calculating theoretical values,
for comparison with experimental results.
"""

def vertical_velocity(A, D, H, f, a, k, h, x, t):
    """
    Calculate the real vertical velocity
    at the top of the plates (z=-H).
    
    Corresponds to the real part of the modified version 
    of Equation 35 in Weber (2025).

    Parameters:
        A : Wave amplitude (m)
        D : total water depth (m)
        H : depth of plate top (m)
        f : wave frequency (Hz)
        a : spatial damping coefficient (1/m)
        k : wavenumber (1/m)
        h : plate spacing (m)
        x: horizontal position (m)
        t: time (s)

    Returns:
        w : average vertical velocity (m/s)
    """

    # Constants
    g = 9.81  # gravitational acceleration (m/s^2)
    nu = 1e-6  # kinematic viscosity of water (m^2/s)

    # Angular frequency
    omega = 2 * np.pi * f

    # Phase
    theta = k*x - omega*t - 2.5

    term1 = 2 * (g*H)**0.5 * A * np.exp(-a*x) * a
    term2 = (((omega*h**2*D)/(12*H*nu))*np.sin(theta) - np.cos(theta))
    w = term1 * term2
    return w

def vertical_velocity_2(A, D, H, f, a, k, h, x, t):
    """
    Calculate the real vertical velocity
    at the top of the plates (z=-H).

    Parameters:
        A : Wave amplitude (m)
        D : total water depth (m)
        H : depth of plate top (m)
        f : wave frequency (Hz)
        a : spatial damping coefficient (1/m)
        k : wavenumber (1/m)
        h : plate spacing (m)
        x: horizontal position (m)
        t: time (s)

    Returns:
        w : average vertical velocity (m/s)
    """

    # Constants
    g = 9.81  # gravitational acceleration (m/s^2)
    nu = 1e-6  # kinematic viscosity of water (m^2/s)

    # Angular frequency
    omega = 2 * np.pi * f

    # Phase
    theta = k*x - omega*t - 2.5

    nominator = g*(D - H)*A*np.exp(-a*x)
    denominator = omega**2 + (144*nu**2)/(h**4)
    B = ((12*k**2*nu*np.cos(theta))/(h**2)) - omega*k**2*np.sin(theta) - 2*omega*a*k*np.cos(theta) - ((24*a*k*nu*np.sin(theta))/(h**2))

    return nominator*B/denominator

# Airy theory velocities
def w_airy(A, f, k, D, H, x, t):
    # At z = -H
    omega = 2*np.pi*f
    return (A*omega) * ((np.sinh(k*(-H + D))/(np.sinh(k*D))))*np.sin(k*x - omega*t - 2.5)

def u_airy(A, f, k, D, H, x, t):
    # At z = -H
    omega = 2*np.pi*f
    return (A*omega) * ((np.cosh(k*(-H + D))/(np.sinh(k*D))))*np.cos(k*x - omega*t - 2.5)

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

def wave_number_in_theory(f, H):
    # Approximation of 58* (modifed eq 58 in Weber (2025)) 
    g = 9.81
    omega = 2*np.pi*f
    return omega/np.sqrt(g*H)


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
    
    return alpha, alpha_weber


def robin_parameter_eq_39(H, a, k):
    """
    Calculate the Robin boundary condition parameter R.
    Corresponds to the modified version of Equation 60 in Weber (2025).

    Parameters:
        H : depth of plate top (m)
        a : spatial damping coefficient (1/m)
        k : wavenumber (1/m)

    Returns:
        R : Robin parameter (m)
    """
    R = (2*H*a)/(k)

    return R

def robin_parameter_eq_28(f, a, k, H):
    omega = 2*np.pi*f
    g = 9.81
    
    P = omega/(2*k) * (1 + g*(k**2)*H/(omega**2) - (omega**2)*H/g)
    frac1 = (2*omega*a*P) / (g*(k**2))
    frac2 = 1/(1 - np.tanh(k*H)**2)

    return frac1 * frac2
