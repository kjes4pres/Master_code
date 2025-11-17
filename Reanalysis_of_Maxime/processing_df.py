import pandas as pd
import numpy as np

def process_and_modify(df, tol=1e-6, max_gap=4, passes=2):
    '''
    Processes the DataFrame by removing noise, converting timestamps to datetime values,
    correcting for large outliers, and smoothing the data.
    '''
    # DataFrame headers
    headers = ['time', 'p1', 'p2', 'p3', 'p4', 'speed of sound']
    df.columns = headers


    # Removing noise and converting timestamps
    for col in range(1, 5):
        noise = df.iloc[:200, col].mean()
        df.iloc[:, col] = df.iloc[:, col] - noise

    df['time'] = pd.to_datetime(df['time'])

    # Applying low pass filter
    weights = np.array([0.1, 0.2, 0.4, 0.2, 0.1])
    df_smooth = df.copy()

    for col in df_smooth.columns[1:5]:
        values = df_smooth[col].values.astype(float).copy()

        # Outlier correction
        n = len(values)
        for gap in range(1, max_gap + 1):
            for i in range(1, n - gap - 1):
                left = values[i - 1]
                right = values[i + gap]
                if abs(left - right) < tol:
                    middle = values[i:i + gap]
                    if all(abs(m - left) > tol for m in middle):
                        values[i:i + gap] = left

        # Smoothing with weighted moving average
        for _ in range(passes):
            smoothed = values.copy()
            for i in range(2, len(values) - 2):
                window = values[i-2:i+3]
                smoothed[i] = np.dot(weights, window)
            values = smoothed

        df_smooth[col] = values
    
    return df_smooth

def combine_runs(*dfs):
    combined_df = pd.concat(dfs).groupby(level=0).mean()

    return combined_df