import pandas as pd
import numpy as np
import os
import sys

sys.path.append('/Users/kjesta/Desktop/LABDATA/Kjersti_280126/')
sys.path.append('/Users/kjesta/Desktop/Master prosjekt/Master_code/Lab/')
sys.path.append('/Users/kjesta/Desktop/Master prosjekt/Processed_files/')

from funcs import *
from processing_funcs import *
from analysis_funcs import *

"""
This script collects the amplitude results from different experiments (3 runs per experiment) and saves them into text files for easier access and comparison.
The experiments vary by frequency, amplitude, water depth and plate configuration.
The experiment files have already been processed to extract the relevant amplitude data.

Example file names to give as argument when running the script:
'20cm_f11_a01' for frequency 1.1 Hz, amplitude 0.1 V, water depth 20 cm, no plates
'20cm_f11_a01_p005' for frequency 1.1 Hz, amplitude 0.1 V, water depth 20 cm, with 5 cm tall plates

The script reads the processed CSV files for each run, extracts the amplitude data, and writes it to a text file in the specified output folder.
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

    # Get the amplitude and error lists for each run
    amps_r1, errs_r1 = get_amp_n_err_lists(r1)
    amps_r2, errs_r2 = get_amp_n_err_lists(r2)
    amps_r3, errs_r3 = get_amp_n_err_lists(r3)

    print("Amplitudes and errors extracted from processed files.")

    # Get observed spatial damping coefficients for each run
    x_probe_pos = np.array([4.86, 6.69, 7.87, 9.15])  # positions of probes in meters from wave maker
    alpha_r1, se_alpha_r1, t_val_r1 = get_obs_damping_coeff(amps_r1, x_probe_pos)
    alpha_r2, se_alpha_r2, t_val_r2 = get_obs_damping_coeff(amps_r2, x_probe_pos)
    alpha_r3, se_alpha_r3, t_val_r3 = get_obs_damping_coeff(amps_r3, x_probe_pos)
    print("Observed damping coefficients calculated.")

    # Find change in amplitude from first to last probe for each run
    P3_minus_P0_r1 = amps_r1[3] - amps_r1[0]
    P3_minus_P0_r2 = amps_r2[3] - amps_r2[0]
    P3_minus_P0_r3 = amps_r3[3] - amps_r3[0]

    results = []

    results.append({'Run': 'R1',
                    'Alpha_obs': alpha_r1,
                    'SE_Alpha_obs': se_alpha_r1,
                    'T_val': t_val_r1,
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
                    'T_val': t_val_r2,
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
                    'T_val': t_val_r3,
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

