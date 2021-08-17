import os
import argparse

def rename_file(mother_folder):

    for folder in os.listdir(mother_folder):
        folder_path=os.path.join(mother_folder, folder)
        print ('folder_path:', folder_path)
        for file in os.listdir(folder_path):
            if 'depleted' not in file:
                path = os.path.join(folder_path, file)
                os.remove(path)
            if "depleted" in file:
                old_file = os.path.join(folder_path, file)
                new_file = os.path.join(folder_path, file[0:-13])
                os.rename(old_file, new_file)
            


parser = argparse.ArgumentParser()
parser.add_argument('mother_folder', type=str, help='A file to print')
args = parser.parse_args()

rename_file(args.mother_folder)