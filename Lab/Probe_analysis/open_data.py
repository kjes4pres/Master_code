import pandas as pd
import sys
sys.path.append('/Users/kjesta/Desktop/Master prosjekt/')

import pandas as pd

processed_data_20cm = {
    1.1: {
        0.1: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a01_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a01_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a01_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a01_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a01_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a01_p005_r3_processed.csv"),
            },
        },
        0.2: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a02_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a02_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a02_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a02_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a02_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a02_p005_r3_processed.csv"),
            },
        },
        0.3: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a03_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a03_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a03_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a03_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a03_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f11_a03_p005_r3_processed.csv"),
            },
        },
    },

    1.2: {
        0.1: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a01_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a01_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a01_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a01_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a01_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a01_p005_r3_processed.csv"),
            },
        },
        0.2: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a02_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a02_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a02_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a02_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a02_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a02_p005_r3_processed.csv"),
            },
        },
        0.3: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a03_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a03_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a03_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a03_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a03_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f12_a03_p005_r3_processed.csv"),
            },    
        },
    },

    1.3: {
        0.1: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a01_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a01_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a01_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a01_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a01_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a01_p005_r3_processed.csv"),
            },
        },
        0.2: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a02_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a02_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a02_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a02_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a02_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a02_p005_r3_processed.csv"),
            },
        },
        0.3: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a03_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a03_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a03_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a03_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a03_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f13_a03_p005_r3_processed.csv"),
            },
        },
    },

    1.4: {
        0.1: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a01_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a01_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a01_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a01_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a01_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a01_p005_r3_processed.csv"),
            },
        },
        0.2: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a02_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a02_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a02_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a02_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a02_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a02_p005_r3_processed.csv"),
            },
        },
        0.3: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a03_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a03_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a03_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a03_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a03_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f14_a03_p005_r3_processed.csv"),
            },
        },
    },

    1.5: {
        0.1: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a01_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a01_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a01_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a01_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a01_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a01_p005_r3_processed.csv"),
            },
        },
        0.2: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a02_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a02_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a02_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a02_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a02_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a02_p005_r3_processed.csv"),
            },
        },
        0.3: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a03_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a03_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a03_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a03_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a03_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f15_a03_p005_r3_processed.csv"),
            },
        },
    },

    1.6: {
        0.1: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a01_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a01_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a01_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a01_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a01_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a01_p005_r3_processed.csv"),
            },
        },
        0.2: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a02_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a02_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a02_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a02_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a02_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a02_p005_r3_processed.csv"),
            },
        },
        0.25: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a025_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a025_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a025_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a025_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a025_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a025_p005_r3_processed.csv"),
            },
        },
        0.3: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a03_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a03_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a03_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a03_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a03_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f16_a03_p005_r3_processed.csv"),
            },
        },
    },

    1.7: {
        0.1: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a01_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a01_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a01_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a01_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a01_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a01_p005_r3_processed.csv"),
            },
        },
        0.2: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a02_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a02_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a02_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a02_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a02_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a02_p005_r3_processed.csv"),
            },
        },
        0.25: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a025_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a025_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a025_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a025_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a025_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a025_p005_r3_processed.csv"),
            },
        },
        0.3: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a03_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a03_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a03_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a03_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a03_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f17_a03_p005_r3_processed.csv"),
            },
        },
    },

    1.8: {
        0.1: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a01_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a01_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a01_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a01_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a01_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a01_p005_r3_processed.csv"),
            },
        },
        0.2: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a02_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a02_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a02_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a02_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a02_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a02_p005_r3_processed.csv"),
            },
        },
        0.25: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a025_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a025_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a025_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a025_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a025_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a025_p005_r3_processed.csv"),
            },
        },
        0.3: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a03_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a03_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a03_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a03_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a03_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/20cm_f18_a03_p005_r3_processed.csv"),
            },
        },
    },
}


processed_data_30cm = {
    0.898: {
        0.149: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0149_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0149_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0149_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0149_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0149_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0149_p005_r3_processed.csv"),
            },
        },
        0.299: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0299_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0299_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0299_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0299_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0299_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0299_p005_r3_processed.csv"),
            },
        },
        0.453: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0453_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0453_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0453_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0453_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0453_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0898_a0453_p005_r3_processed.csv"),
            },
        },
    },

    0.980: {
        0.149: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0149_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0149_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0149_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0149_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0149_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0149_p005_r3_processed.csv"),
            },
        },
        0.295: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0295_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0295_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0295_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0295_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0295_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0295_p005_r3_processed.csv"),
            },
        },
        0.443: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0443_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0443_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0443_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0443_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0443_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f0980_a0443_p005_r3_processed.csv"),
            },
        },
    },

    1.061: {
        0.149: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0149_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0149_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0149_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0149_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0149_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0149_p005_r3_processed.csv"),
            },
        },
        0.295: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0295_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0295_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0295_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0295_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0295_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0295_p005_r3_processed.csv"),
            },
        },
        0.449: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0449_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0449_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0449_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0449_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0449_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1061_a0449_p005_r3_processed.csv"),
            },
        },
    },

    1.143: {
        0.148: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0148_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0148_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0148_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0148_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0148_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0148_p005_r3_processed.csv"),
            },
        },
        0.295: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0295_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0295_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0295_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0295_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0295_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0295_p005_r3_processed.csv"),
            },
        },
        0.443: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0443_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0443_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0443_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0443_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0443_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1143_a0443_p005_r3_processed.csv"),
            },
        },
    },

    1.225: {
        0.152: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0152_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0152_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0152_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0152_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0152_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0152_p005_r3_processed.csv"),
            },
        },
        0.299: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0299_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0299_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0299_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0299_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0299_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0299_p005_r3_processed.csv"),
            },
        },
        0.471: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0471_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0471_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0471_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0471_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0471_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1225_a0471_p005_r3_processed.csv"),
            },
        },
    },

    1.306: {
        0.152: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0152_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0152_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0152_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0152_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0152_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0152_p005_r3_processed.csv"),
            },
        },
        0.302: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0302_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0302_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0302_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0302_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0302_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0302_p005_r3_processed.csv"),
            },
        },
        0.372: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0372_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0372_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0372_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0372_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0372_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0372_p005_r3_processed.csv"),
            },
        },
        0.461: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0461_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0461_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0461_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0461_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0461_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1306_a0461_p005_r3_processed.csv"),
            },
        },
    },

    1.388: {
        0.147: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0147_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0147_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0147_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0147_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0147_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0147_p005_r3_processed.csv"),
            },
        },
        0.285: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0285_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0285_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0285_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0285_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0285_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0285_p005_r3_processed.csv"),
            },
        },
        0.378: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0378_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0378_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0378_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0378_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0378_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0378_p005_r3_processed.csv"),
            },
        },
        0.468: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0468_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0468_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0468_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0468_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0468_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1388_a0468_p005_r3_processed.csv"),
            },
        },
    },

    1.470: {
        0.147: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0147_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0147_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0147_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0147_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0147_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0147_p005_r3_processed.csv"),
            },
        },
        0.296: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0296_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0296_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0296_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0296_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0296_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0296_p005_r3_processed.csv"),
            },
        },
        0.382: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0382_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0382_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0382_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0382_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0382_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0382_p005_r3_processed.csv"),
            },
        },
        0.459: {
            "None": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0459_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0459_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0459_r3_processed.csv"),
            },
            "p005": {
                "R1": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0459_p005_r1_processed.csv"),
                "R2": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0459_p005_r2_processed.csv"),
                "R3": pd.read_csv("/Users/kjesta/Desktop/LABDATA/Processed_files/30cm_f1470_a0459_p005_r3_processed.csv"),
            },
        },
    },
}
