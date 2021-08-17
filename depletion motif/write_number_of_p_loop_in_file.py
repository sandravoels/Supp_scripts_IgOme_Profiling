import regex
import pandas as pd
import os
from Bio import SeqIO
import argparse

#output in C:\Users\JonathanG03
#writes the rpm of pentameric loop into one file

def deplete_p_loop(mother_folder):
    number_of_p_loops_file = open("number_of_p_loops.txt","w")
    for folder in os.listdir(mother_folder):
        folder_path=os.path.join(mother_folder, folder)
        print ('folder_path:', folder_path)
        for file in os.listdir(folder_path):
            if "depleted" not in file:
                number_of_p_loops_file.write('\n')
                path = os.path.join(folder_path, file)
                print("file_path:", path)
                number_of_p_loops_file.write(path[-30:-1])
                number_of_p_loops_file.write('\t')

                list_sequences = []
                rpm = []

                with open(path, 'r') as f:  

                        n=0
                        m=1

                        for i, line in enumerate(f):
                            if i == n:
                                rpm.append(line)
                                n+=2             
                            if i == m:
                                list_sequences.append(line[:-1])
                                m+=2
                            #if i>10002:
                                #break
                            
                df_read = pd.DataFrame(
                    {'sequence_read': list_sequences,
                    'rpm': rpm
                    })

                def find_rpm(rpm_line):
                    matches = regex.search('(counts_)',rpm_line)
                    index_end = matches.end()
                    return index_end

                df_read['rpm_end']=df_read['rpm'].apply(find_rpm)
                df_read['rpm'] = df_read.apply(lambda x: x['rpm'][x['rpm_end']:-1], 1)

                df_read['rpm']=df_read['rpm'].astype(str).astype(float)

                assert 999999<df_read['rpm'].sum()<1000001, "sum of RPM is not 1000000"

                def find_pentameric_loop(sequence):
                    matches = regex.search('(C.G...C)', sequence)
                    if matches !=None:
                        return ('pentameric loop')

                df_read['pentameric_loop'] = df_read['sequence_read'].apply(find_pentameric_loop)

                groups=df_read.groupby('pentameric_loop')
                df_rpm_pentameric_loop=df_read.groupby('pentameric_loop')['rpm'].apply(sum)
                print(df_rpm_pentameric_loop)
                number_of_p_loops_file.write(str(df_rpm_pentameric_loop.tolist()))
            

parser = argparse.ArgumentParser()
parser.add_argument('mother_folder', type=str, help='A file to print')
args = parser.parse_args()

deplete_p_loop(args.mother_folder)