import numpy as np 
import pandas as pd 
import os
import librosa
from my_memory_profiler import profile


# @profile
def num_seg(data_dir, audio_labels, SAMPLE_RATE, output_csv=None, filenames=False):
    time_leng=0.4
    sample_leng=int(time_leng*SAMPLE_RATE)
    overloap=2
    segments_info=[]
    # audio_labels=pd.read_csv('labels.csv')


    #Processs data to train
    for data_ind, audio_label in enumerate(audio_labels.values):
        file_name=audio_label[-1]
        data_path=os.path.join(data_dir, file_name)
        audio, sample_rate = librosa.load(data_path, sr=SAMPLE_RATE)
        audio_len=len(audio)
        #print(audio_len)
        #plt.plot(audio)
        audio=audio/np.max(abs(audio))
        indx=[i for i,x in enumerate(np.sqrt(abs(audio))) if x>.30]
        segments=0
        if (indx[0]+sample_leng)<audio_len:
            for i in range(int((-indx[0]+indx[len(indx)-1])/(sample_leng/overloap))):
                ind_start = i * int(sample_leng/overloap)+indx[0]
                ind_end = ind_start + sample_leng
                if ind_end <= indx[-1]:
                    segments+=1
            if filenames:
                segments_info.append({
                    'Filename': file_name,
                    'Segments': segments})
            else: 
                segments_info.append({'Segments':segments})
            
            print(" Processed {}/{} files".format(data_ind,2902),end='\n')
        else:
            print(" Processed {}/{} files".format(data_ind,2902),end='\n')
            if filenames:
                segments_info.append({
                    'Filename': file_name,
                    'Segments': segments})
            else: 
                segments_info.append({'Segments':segments})
    

    df_segments = pd.DataFrame(segments_info)
    if(output_csv is None):
        return df_segments
    else:
        df_segments.to_csv(output_csv, index=False)
        