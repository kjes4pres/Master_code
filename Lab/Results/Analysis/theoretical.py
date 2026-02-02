import numpy as np
import pandas as pd

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


