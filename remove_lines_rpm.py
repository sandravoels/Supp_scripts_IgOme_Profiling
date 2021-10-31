import os
from Bio import SeqIO
import argparse


def remove_lines(mother_folder): #function

    for folder in os.listdir(mother_folder): #mother folfer path
        folder_path=os.path.join(mother_folder, folder) #create path to subfolder
        #print ('folder_path:', folder_path)
        for file in os.listdir(folder_path): # run file by file in subfolder
            if "new" not in file: # "new" is the name of the new file that this script come out
                path = os.path.join(folder_path, file) # path file
                #print("file_path:", path)
                fasta_sequences =SeqIO.parse(path,'fasta') #fasta file handle
                rpm=[] # new list
                new=[] # new list
                for fasta_entry in fasta_sequences: #fasta_entry -> two lines
                    x=(fasta_entry.id[26:-1]).strip('counts_')# rpm
                    rpm.append(x) # append to list rpm 
                min_rpm=(float(rpm[-1])*3) # min rpm we want is (min_rpm*3)
                fasta_sequences =SeqIO.parse(path,'fasta') # come back to beginning of the file
                for fasta_entry in fasta_sequences:
                    
                    if (float((fasta_entry.id[26:-1]).strip('counts_')) > min_rpm): # if rpm > min_rpm
                        new.append(fasta_entry) #append to list 
                        

                with open(path+"_new.faa", "w") as output_handle:
                    SeqIO.write(new, output_handle, "fasta") #erite "new" list to file

parser = argparse.ArgumentParser()
parser.add_argument('mother_folder', type=str, help='mother folder that have subfolders with file')
args = parser.parse_args()

remove_lines(args.mother_folder)
