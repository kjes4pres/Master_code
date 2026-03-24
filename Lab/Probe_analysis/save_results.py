from fileinput import filename

import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import scipy as sc

sys.path.append('/Users/kjesta/Desktop/LABDATA/')
sys.path.append('/Users/kjesta/Desktop/Master prosjekt/Master_code/')

from Lab.funcs import *
from Lab.processing_funcs import *
from Lab.analysis_funcs import *

"""
This script collects the amplitude results from different experiments (3 runs per experiment) and saves them into csv files for easier access and comparison.
The experiments vary by frequency, amplitude, water depth and plate configuration.
The experiment files have already been processed to extract the relevant amplitude data.

Example file names to give as argument when running the script:
'20cm_f11_a01' for frequency 1.1 Hz, amplitude 0.1 V, water depth 20 cm, no plates
'20cm_f11_a01_p005' for frequency 1.1 Hz, amplitude 0.1 V, water depth 20 cm, with 5 cm tall plates

The script reads the processed CSV files for each run, extracts the amplitude data, and writes it to a csv file in the specified output folder.
"""
def __main__():
    if len(sys.argv) != 2:
        print("You must provide the file to process as an argument.")
        sys.exit(1)
    print("File to extract amplitudes from:", sys.argv[1])

    # Where to save the output files
    output_folder = '/Users/kjesta/Desktop/LABDATA/Calculated_amps/'

    # Where to find the processed CSV files
    base_path = '/Users/kjesta/Desktop/LABDATA/Processed_files/'

    # Frequency of given file
    filename = os.path.basename(sys.argv[1])
    # '20cm_f11_a01' -> ['20cm', 'f11', 'a01']
    parts = filename.split('_')
    freq_str = parts[1]      # 'f11'
    freq = float(freq_str[1:]) / 10.0   # drop 'f', '11' -> 1.1

    print(freq)

    # Open the processed CSV files for the three runs
    r1 = pd.read_csv(os.path.join(base_path, sys.argv[1] + '_r1_processed.csv'))
    r2 = pd.read_csv(os.path.join(base_path, sys.argv[1] + '_r2_processed.csv'))
    r3 = pd.read_csv(os.path.join(base_path, sys.argv[1] + '_r3_processed.csv'))

    # Check that the processed files look good
    # Aka that the post-processing worked as intended
    for col in ['P_0', 'P_1', 'P_2', 'P_3']:
        if np.mean(r1[col]) > 1e-15 or np.mean(r2[col]) > 1e-15 or np.mean(r3[col]) > 1e-15:
            raise ValueError(f"Column {col} mean is not zero in one of the runs, check processing.")
        else:
            print(f"Column {col} mean check passed :)")

    # The measurements are the distance from the water surface to the probe
    # In post-processing, the mean of each column was set to zero to have
    # have the surface wave oscillate around zero.
    # Therefore, negative values in the columns correspond to the positive amplitude of the wave.

    # Fixing the sign of the amplitudes to be positive
    r1[['P_0', 'P_1', 'P_2', 'P_3']] = (-1) * r1[['P_0', 'P_1', 'P_2', 'P_3']]
    r2[['P_0', 'P_1', 'P_2', 'P_3']] = (-1) * r2[['P_0', 'P_1', 'P_2', 'P_3']]
    r3[['P_0', 'P_1', 'P_2', 'P_3']] = (-1) * r3[['P_0', 'P_1', 'P_2', 'P_3']]

    # Expected distance between peaks in samples, based on the frequency and sample rate of 250 Hz
    distance = (1/freq) * 250 * 0.8

    # Identify peaks in the data for each probe and run, using scipy's find_peaks function 
    # with a height threshold based on the standard deviation of the signal
    # Keeping only the positive peaks
    p0_peaks_r1 = find_positive_peaks(freq, r1, 'P_0')
    p0_peaks_r2 = find_positive_peaks(freq, r2, 'P_0')
    p0_peaks_r3 = find_positive_peaks(freq, r3, 'P_0')

    p1_peaks_r1 = find_positive_peaks(freq, r1, 'P_1')
    p1_peaks_r2 = find_positive_peaks(freq, r2, 'P_1')  
    p1_peaks_r3 = find_positive_peaks(freq, r3, 'P_1')

    p2_peaks_r1 = find_positive_peaks(freq, r1, 'P_2')
    p2_peaks_r2 = find_positive_peaks(freq, r2, 'P_2')
    p2_peaks_r3 = find_positive_peaks(freq, r3, 'P_2')

    p3_peaks_r1 = find_positive_peaks(freq, r1, 'P_3')
    p3_peaks_r2 = find_positive_peaks(freq, r2, 'P_3')
    p3_peaks_r3 = find_positive_peaks(freq, r3, 'P_3')

    # Get the observed amplitude and error for each probe and run
    mean_amp_p0_r1, err_amp_p0_r1 = mean_amp_and_err(p0_peaks_r1)
    mean_amp_p0_r2, err_amp_p0_r2 = mean_amp_and_err(p0_peaks_r2)
    mean_amp_p0_r3, err_amp_p0_r3 = mean_amp_and_err(p0_peaks_r3)

    mean_amp_p1_r1, err_amp_p1_r1 = mean_amp_and_err(p1_peaks_r1)
    mean_amp_p1_r2, err_amp_p1_r2 = mean_amp_and_err(p1_peaks_r2)
    mean_amp_p1_r3, err_amp_p1_r3 = mean_amp_and_err(p1_peaks_r3)

    mean_amp_p2_r1, err_amp_p2_r1 = mean_amp_and_err(p2_peaks_r1)
    mean_amp_p2_r2, err_amp_p2_r2 = mean_amp_and_err(p2_peaks_r2)
    mean_amp_p2_r3, err_amp_p2_r3 = mean_amp_and_err(p2_peaks_r3)

    mean_amp_p3_r1, err_amp_p3_r1 = mean_amp_and_err(p3_peaks_r1)
    mean_amp_p3_r2, err_amp_p3_r2 = mean_amp_and_err(p3_peaks_r2)
    mean_amp_p3_r3, err_amp_p3_r3 = mean_amp_and_err(p3_peaks_r3)

    amps_r1 = [mean_amp_p0_r1, mean_amp_p1_r1, mean_amp_p2_r1, mean_amp_p3_r1]
    amps_r2 = [mean_amp_p0_r2, mean_amp_p1_r2, mean_amp_p2_r2, mean_amp_p3_r2]
    amps_r3 = [mean_amp_p0_r3, mean_amp_p1_r3, mean_amp_p2_r3, mean_amp_p3_r3]

    errs_r1 = [err_amp_p0_r1, err_amp_p1_r1, err_amp_p2_r1, err_amp_p3_r1]
    errs_r2 = [err_amp_p0_r2, err_amp_p1_r2, err_amp_p2_r2, err_amp_p3_r2]
    errs_r3 = [err_amp_p0_r3, err_amp_p1_r3, err_amp_p2_r3, err_amp_p3_r3]

    print("Amplitudes and errors extracted from processed files.")

    # Get observed spatial damping coefficients for each run
    x_probe_pos = np.array([4.86, 6.69, 7.87, 9.15])  # positions of probes in meters from wave maker

    alpha_r1, se_alpha_r1= get_obs_damping_coeff(amps_r1, x_probe_pos)
    alpha_r2, se_alpha_r2 = get_obs_damping_coeff(amps_r2, x_probe_pos)
    alpha_r3, se_alpha_r3 = get_obs_damping_coeff(amps_r3, x_probe_pos)
    print("Observed damping coefficients calculated.")

    # Find change in amplitude from first to last probe for each run
    P3_minus_P0_r1 = amps_r1[3] - amps_r1[0]
    P3_minus_P0_r2 = amps_r2[3] - amps_r2[0]
    P3_minus_P0_r3 = amps_r3[3] - amps_r3[0]

    results = []

    results.append({'Run': 'R1',
                    'Alpha_obs': alpha_r1,
                    'SE_Alpha_obs': se_alpha_r1,
                    'Amp_obs_P0': amps_r1[0],
                    'Amp_obs_P1': amps_r1[1],
                    'Amp_obs_P2': amps_r1[2],
                    'Amp_obs_P3': amps_r1[3],
                    'Amp_errors_P0': errs_r1[0],
                    'Amp_errors_P1': errs_r1[1],
                    'Amp_errors_P2': errs_r1[2],
                    'Amp_errors_P3': errs_r1[3],
                    'P3_minus_P0': P3_minus_P0_r1})
    results.append({'Run': 'R2',
                    'Alpha_obs': alpha_r2,
                    'SE_Alpha_obs': se_alpha_r2,
                    'Amp_obs_P0': amps_r2[0],
                    'Amp_obs_P1': amps_r2[1],
                    'Amp_obs_P2': amps_r2[2],
                    'Amp_obs_P3': amps_r2[3],
                    'Amp_errors_P0': errs_r2[0],
                    'Amp_errors_P1': errs_r2[1],
                    'Amp_errors_P2': errs_r2[2],
                    'Amp_errors_P3': errs_r2[3],
                    'P3_minus_P0': P3_minus_P0_r2})
    results.append({'Run': 'R3',
                    'Alpha_obs': alpha_r3,
                    'SE_Alpha_obs': se_alpha_r3,
                    'Amp_obs_P0': amps_r3[0],
                    'Amp_obs_P1': amps_r3[1],
                    'Amp_obs_P2': amps_r3[2],
                    'Amp_obs_P3': amps_r3[3],
                    'Amp_errors_P0': errs_r3[0],
                    'Amp_errors_P1': errs_r3[1],
                    'Amp_errors_P2': errs_r3[2],   
                    'Amp_errors_P3': errs_r3[3],
                    'P3_minus_P0': P3_minus_P0_r3})
    
    # Save the results to csv file
    df = pd.DataFrame(results)
    output_file = os.path.join(output_folder, sys.argv[1] + '_results.csv')
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    __main__()

