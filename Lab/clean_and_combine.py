'''
For a given experiment with three runs, I pre-process the data.

1) Clean each run by removing gauge noise and converting timestamps.
    That is, for each pressure probe column, I subtract the mean of the first 100 rows (gauge noise).
    Then, I convert the timestamps to seconds starting from zero.
2) Apply low-pass filter to each cleaned run.
    The low-pass filter is applied in the same way as done by Maxime:
    - First, correct for large outliers by checking gaps up to size 4 and replacing values in between if the values on both sides are close enough.
    - Then, apply a weighted moving average filter with weights [0.1, 0.2, 0.4, 0.2, 0.1] for 2 passes.
3) Detrend each filtered run (set mean to zero).
'''

import pandas as pd
import numpy as np


def clean(df):
    '''
    Removes noise from data by subtracting the mean of the first 100 rows,
    and converts timestamps to datetime values.
    '''
    df['time'] = df.iloc[:, 0]
    # Removing noise
    for col in range(1, 5):
        noise = df.iloc[:100, col].mean()
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

# Applying low pass filter in the same style as Maxime
weights = np.array([0.1, 0.2, 0.4, 0.2, 0.1])

def low_pass(df, tol=1e-6, max_gap=4, passes=2):
    ''' 
    Corrects for large outliers and smoothes the data
    '''
    df_smooth = df.copy()

    for col in df_smooth.columns[1:5]:
        values = df_smooth[col].values.astype(float).copy()

        n = len(values)
        for gap in range(1, max_gap + 1):
            for i in range(1, n - gap - 1):
                left = values[i - 1]
                right = values[i + gap]
                if abs(left - right) < tol:
                    middle = values[i:i + gap]
                    if all(abs(m - left) > tol for m in middle):
                        values[i:i + gap] = left

        for _ in range(passes):
            smoothed = values.copy()
            for i in range(2, len(values) - 2):
                window = values[i-2:i+3]
                smoothed[i] = np.dot(weights, window)
            values = smoothed

        df_smooth[col] = values
    
    return df_smooth