import regex
import os
from Bio import SeqIO
import argparse

def deplete_p_loop(mother_folder):

    for folder in os.listdir(mother_folder):
        folder_path=os.path.join(mother_folder, folder)
        print ('folder_path:', folder_path)
        for file in os.listdir(folder_path):
            if "depleted" not in file:
                path = os.path.join(folder_path, file)
                print("file_path:", path)

                fasta_sequences = SeqIO.parse(path,'fasta')

                depleted_list=[]

                for fasta_entry in fasta_sequences:
                    matches = regex.search('(C.G...C)', str(fasta_entry.seq))
                    if matches ==None:
                        depleted_list.append(fasta_entry)

                with open(path+"_depleted3.faa", "w") as output_handle:
                    SeqIO.write(depleted_list, output_handle, "fasta")



parser = argparse.ArgumentParser()
parser.add_argument('mother_folder', type=str, help='A file to print')
args = parser.parse_args()

deplete_p_loop(args.mother_folder)