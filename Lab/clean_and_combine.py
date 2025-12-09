'''
For a given experiment with three runs, I pre-process the data.

1) Clean each run by removing gauge noise and converting timestamps.
    That is, for each pressure probe column, I subtract the mean of the first 500 rows (gauge noise).
    Then, I convert the timestamps to seconds starting from zero.
2) Detrend each filtered run (set mean to zero).

If needed:
3) Correct for large outliers in the data.

'''

import pandas as pd
import numpy as np


def clean(df):
    '''
    Removes noise from data by subtracting the mean of the first 500 rows,
    and converts timestamps to datetime values.
    '''
    df['time'] = df.iloc[:, 0]
    # Removing noise
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
    '''
    df_detrended = df.copy()
    for col in df_detrended.columns[1:5]:
        df_detrended[col] = df_detrended[col] - np.mean(df_detrended[col])
    return df_detrended


def outlier_correction(df, tol=1e-6, max_gap=10):
    '''
    Corrects for large outliers in the data.
    Parameters:
    df : pandas DataFrame
        DataFrame containing the data to be corrected.
    tol : float
        Tolerance for detecting outliers.
    max_gap : int
        Maximum gap size to consider for outlier correction.
    Returns:
    pandas DataFrame
        Corrected DataFrame.
    ''' 
    df_corrected = df.copy()
    # Process each probe column
    for col in df_corrected.columns[1:5]:
        # Extract values as a float numpy array
        values = df_corrected[col].values.astype(float).copy()

        n = len(values)
        # Correct for large outliers by checking gaps up to size max_gap
        for gap in range(1, max_gap + 1):
            for i in range(1, n - gap - 1):
                left = values[i - 1]
                right = values[i + gap]
                # If left and right are close enough, replace middle values
                if abs(left - right) < tol:
                    middle = values[i:i + gap]
                    # Check if all middle values are far from left/right
                    if all(abs(m - left) > tol for m in middle):
                        values[i:i + gap] = left

        df_corrected[col] = values

    return df_corrected

def correct_outliers(df):
    df_corrected = df.copy()
    for col in df_corrected.columns[1:5]:
        values = df_corrected[col].values
        mean = np.mean(values)
        std = np.std(values)
        # Identify outliers
        outliers = np.abs(values - mean) / std > 3 
        # Replace outliers with neighboring mean
        for i in range(len(values)):
            if outliers[i]:
                if i == 0:
                    values[i] = values[i + 1]
                elif i == len(values) - 1:
                    values[i] = values[i - 1]
                else:
                    values[i] = (values[i - 1] + values[i + 1]) / 2
        df_corrected[col] = values
    return df_corrected
