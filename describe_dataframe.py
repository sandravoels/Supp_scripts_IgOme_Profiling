import os
import argparse
import numpy as np
import pandas as pd

def rename_file(mother_folder): #fun: argument:folder with sub-folders
    list_name=[] #name per barcode
    list_max=[] #max rpm
    list_min=[] #min rpm
    list_mean=[] #mean rpm
    list_median=[] #median rpm

    for folder in os.listdir(mother_folder): #pass folder by folder
        folder_path=os.path.join(mother_folder, folder) #create path to sub-folder -> "shirshur"
        list_name.append(folder) #append to list
        #print ('folder_path:', folder_path)
        for file in os.listdir(folder_path): #file in sub folder
            list_sequences = []
            rpm = []
            
            #nae data frame: seq, rpm
            with open (os.path.join(folder_path ,file ), 'r') as f: 
                
                n=0
                m=1
                for i, line in enumerate(f):
                    if i == n:
                        rpm.append(line[27:-1])
                        n+=2             
                    if i == m:
                        list_sequences.append(line[:-1])
                        m+=2

            df_read = pd.DataFrame(
                {'sequence_read': list_sequences,
                'rpm': rpm
                })
            
            df_read['rpm']=df_read['rpm'].str.strip('counts_')
            df_read['rpm']= pd.to_numeric(df_read['rpm'], downcast="float")
            #print(df_read.describe())
            list_max.append(df_read['rpm'].max()) #append to list
            list_min.append(df_read['rpm'].min()) #append to list
            list_mean.append(df_read['rpm'].mean()) #append to list
            list_median.append(df_read['rpm'].median()) #append to list
    data=pd.DataFrame(
        {'name': list_name,
        'max': list_max,
        'min': list_min,
        'mean':list_mean,
        'median': list_median
        })
    #print (data)
    data.to_excel(r'C:\Users\JonathanG03\Dropbox\MotifAi_Exercises\Sanofi\exp12\all_data\rf_all_data12\describe.xlsx', index = False) #write to excel
parser = argparse.ArgumentParser()
parser.add_argument('mother_folder', type=str, help='A file to print') #semt argument to fun
args = parser.parse_args()

rename_file(args.mother_folder) # function!