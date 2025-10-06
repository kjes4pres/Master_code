'''
For a given experiment with three runs, I clean the data, apply low-pass filter and take the mean of the three runs. 
The result is written to a new CSV file. Cleaning is done by subtracting gauge noise (column mean for the first 100 
rows) from each column.
'''

import pandas as pd
import numpy as np

def main():
    # Insert filepaths to runs for a given experiment
    # If you run the script, a new csv file will be generated and stored in /Results.
    run1 = '/Users/kjesta/Desktop/Master prosjekt/Maxime_sine_greier/Maxime-s-Programs/20 cm/P0/f076/f076_A015_P0_run1.csv'
    run2 = '/Users/kjesta/Desktop/Master prosjekt/Maxime_sine_greier/Maxime-s-Programs/20 cm/P0/f076/f076_A015_P0_run2.csv'
    run3 = '/Users/kjesta/Desktop/Master prosjekt/Maxime_sine_greier/Maxime-s-Programs/20 cm/P0/f076/f076_A015_P0_run3.csv'

    # Insert wanted filename
    output_filename = 'test.csv'

    # Raw
    df1 = pd.read_csv(run1)
    df2 = pd.read_csv(run2)
    df3 = pd.read_csv(run3)

    # Cleaned
    df1_c = clean(df1)
    df2_c = clean(df2)
    df3_c = clean(df3)

    # Filtered 
    df1_c_f = low_pass(df1_c)
    df2_c_f = low_pass(df2_c)
    df3_c_f = low_pass(df3_c)

    # Taking the mean and combining the three runs
    df_comb = combine_runs(df1_c_f, df2_c_f, df3_c_f)

    # Writing it to a file
    write_to_csv(df_comb, output_filename)

def clean(df):
    '''
    Removes noise from data by subtracting the mean of the first 100 rows,
    and converts timestamps to datetime values.
    '''
    # Removing noise
    for col in range(1, 5):
        noise = df.iloc[:100, col].mean()
        df.iloc[:, col] = df.iloc[:, col] - noise

    # Fixing the timestamps
    df['time'] = pd.to_datetime(df['time'])

    return df

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

def combine_runs(df1, df2, df3):
    '''
    Combines the three runs by taking the column-wise mean of the filtered data.
    '''
    # Ensure all three DataFrames have the same structure and alignment
    if not (df1.columns.equals(df2.columns) and df1.columns.equals(df3.columns)):
        raise ValueError("DataFrames have mismatched columns.")

    # Take the mean of the three runs
    combined_df = df1.copy()
    combined_df.iloc[:, 1:] = (df1.iloc[:, 1:] + df2.iloc[:, 1:] + df3.iloc[:, 1:]) / 3

    # Return the combined DataFrame
    return combined_df

def write_to_csv(df, output_filename):
    '''
    Writes the combined DataFrame of all three runs to a CSV file to "/Results".
    '''
    # Define the output directory
    output_dir = '/Users/kjesta/Desktop/Master prosjekt/Master_code/Lab/Results/Test/'

    # Full path to the output file
    output_path = output_dir + output_filename

    # Write to CSV
    df.to_csv(output_path, index=False)
    print(f"File successfully written to: {output_path}")


if __name__ == "__main__":
    main()
