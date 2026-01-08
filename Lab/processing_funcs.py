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

def correct_spikes(df, threshold, max_passes=20):
    """
    Correct spikes in each probe column.
    - threshold: slope threshold for spike detection (same units as data/time).
    - max_passes: maximum iterations to run; stops early if no new spikes found.

    Original code by Anne Raustoel (2012), modified by Karen Samseth (2022), 
    and converted from matlab to Python here.
    """
    df_corrected = df.copy()

    for col in df_corrected.columns[1:5]:
        probe = df_corrected[col].values.astype(float)
        n = probe.size
        t = np.arange(1, n + 1, dtype=float)

        corrected = probe.copy()

        total_removed = 0
        for pass_num in range(1, max_passes + 1):
            removed_this_pass = 0

            for i in range(2, n - 2):
                # If any of the neighbors are already nan, skip this index
                if np.isnan(corrected[i - 1]) or np.isnan(corrected[i]) or np.isnan(corrected[i + 1]):
                    continue

                slope = (corrected[i + 1] - corrected[i - 1]) / (t[i + 1] - t[i - 1])

                if abs(slope) > threshold:
                    for j in (i - 2, i - 1, i, i + 1, i + 2):
                        if 0 <= j < n:
                            if not np.isnan(corrected[j]):
                                corrected[j] = np.nan
                                removed_this_pass += 1

            if removed_this_pass == 0:
                # nothing found -> stop early
                break

            total_removed += removed_this_pass

            # Interpolate over NaNs when enough valid points exist
            # Mask = True if not NaN
            mask = np.invert(np.isnan(corrected))
            if mask.sum() >= 2:
                interp = PchipInterpolator(t[mask], corrected[mask])
                corrected = interp(t)
            else:
                # Not enough points to interpolate: keep what we have and break
                break

        print(f'Column {col}: Removed {total_removed} spikes in {pass_num} passes.')
        df_corrected[col] = corrected

    return df_corrected
