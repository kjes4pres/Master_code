import numpy as np

def get_amp_n_err_lists(df):
    """
    Find the observed amplitude and standard error at each probe.
    """
    std_list = np.array([df['P_0'].std(), df['P_1'].std(), df['P_2'].std(), df['P_3'].std()])
    amp_list = std_list * np.sqrt(2)
    err_list = std_list / np.sqrt(len(df))

    return amp_list, err_list


def get_obs_alpha(amp_list, probe_pos):
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
    # standard error of slope m is sqrt(cov[0,0])
    se_m = np.sqrt(cov[0, 0])
    se_alpha = se_m

    return alpha, se_alpha

