import numpy as np
import pandas as pd
import os

def label_generator(DATA_PATH_NeuroV):
    data_list = []
    
    for dirname, _, filenames in os.walk(DATA_PATH_NeuroV):
        for filename in filenames:
            if filename.endswith('.wav'):  # Check if the file is a WAV file
                identifiers = filename.split('.')[0].split('_')
                Speaker_ID = int(identifiers[-1])
                Label = 1 if identifiers[0] == 'PD' else 0
                data_list.append({
                    "Speaker_ID": Speaker_ID,
                    "Label": Label,
                    "FileName": filename
                })
    
    data_NeuroV = pd.DataFrame(data_list)
        
    return data_NeuroV