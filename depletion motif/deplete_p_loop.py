import regex
import pandas as pd
import os
from Bio import SeqIO
import argparse

#second version. deplete_p_loop_faster is the best and faster version

def deplete_p_loop(mother_folder):

    for folder in os.listdir(mother_folder):
        folder_path=os.path.join(mother_folder, folder)
        print ('folder_path:', folder_path)
        for file in os.listdir(folder_path):
            if "depleted" not in file:
                path = os.path.join(folder_path, file)
                print("file_path:", path)

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

                for group in groups:
                    for item in group:
                        if type(item) !=str:
                            df_new=item

                df_new
                list_of_sequences_for_depletion=df_new['sequence_read'].tolist()

                depleted_list=[]

                fasta_sequences = SeqIO.parse(path,'fasta')

                for fasta_entry in fasta_sequences:
                    if fasta_entry.seq not in list_of_sequences_for_depletion:
                        depleted_list.append(fasta_entry)


                with open(+"_depleted.faa", "w") as output_handle:
                    SeqIO.write(depleted_list, output_handle, "fasta")



parser = argparse.ArgumentParser()
parser.add_argument('mother_folder', type=str, help='A file to print')
#parser.add_argument('motif', type=str, help='motif for depletion')
args = parser.parse_args()

deplete_p_loop(args.mother_folder)