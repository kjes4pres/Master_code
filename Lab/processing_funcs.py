'''
For a given experiment with three runs, I pre-process the data.

1) Clean each run by removing gauge noise and converting timestamps.
    That is, for each pressure probe column, I subtract the mean of the first 500 rows (gauge noise).
    Then, I convert the timestamps to seconds starting from zero.
2) Detrend each filtered run (set mean to zero).

If needed:
3) Correct for large outliers in the data by removing spikes above a given threshold and 
interpolate any missing values using PCHIP interpolation.

'''

import pandas as pd
import numpy as np
from scipy.interpolate import PchipInterpolator


def clean(df):
    '''
    Removes noise from data by subtracting the mean of the first 500 rows,
    and converts timestamps to datetime values.
    '''
    df['time'] = df.iloc[:, 0]
    # Removing noise columnwise
    for col in range(1, 5):
        noise = df.iloc[:500, col].mean()
        df.iloc[:, col] = df.iloc[:, col] - noise

    # Fixing the timestamps
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'] - df['time'].iloc[0] # Starting time is at zero
    df['time'] = df['time'].dt.total_seconds()

    return df

def detrend(df):
    '''
    Detrends the data by removing linear trend from each column.
    Sets the mean water level to zero.
    '''
    df_detrended = df.copy()
    for col in df_detrended.columns[1:5]:
        df_detrended[col] = df_detrended[col] - np.mean(df_detrended[col])
    return df_detrended

def interpolate_missing(df):
    '''
    Interpolates missing values in the DataFrame.
    '''
    df_interpolated = df.copy()
    df_interpolated.interpolate(method='linear', inplace=True)
    return df_interpolated


def correct_spikes(df, threshold):
    """
    Original code by Karen Samseth, written in MATLAB.
    Modified for Python by Kjersti Stangeland.
    """

    df_corrected = df.copy()

    for col in df_corrected.columns[1:5]:
        probe_data = df_corrected[col].values
        n = len(probe_data)
        t = np.arange(1, n+1)
        corrected_probe_data = probe_data.copy()

        np_total = 0
        counter = 0

        while counter < 20:
            counter += 1
            npr = 0

            for i in range(2, n-3):

                # NEW: Outlier detection without sign condition
                slope = abs((corrected_probe_data[i+1] - corrected_probe_data[i]) /
                            (t[i+1] - t[i]))

                if slope > threshold:
                    for j in [i-2, i-1, i, i+1, i+2]:
                        if 0 <= j < n:
                            corrected_probe_data[j] = np.nan
                    npr += 1

            np_total += npr

            # Interpolate over NaNs using PCHIP
            # Mask = True if value is not NaN
            mask = np.invert(np.isnan(corrected_probe_data))
            
            #if mask.sum() < 2:
               # break

            interpolator = PchipInterpolator(t[mask], corrected_probe_data[mask])
            corrected_probe_data = interpolator(t)

        print(f'Column {col}: Removed {np_total} spikes in {counter} passes.')
        df_corrected[col] = corrected_probe_data

    return df_corrected
