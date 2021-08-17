import os
import argparse

def rename_folder(mother_folder):

    for folder in os.listdir(mother_folder):
        if "_depl" not in folder:
            old_folder = os.path.join(mother_folder, folder)
            new_folder = os.path.join(mother_folder, folder + '_depl')
            os.rename(old_folder, new_folder)


parser = argparse.ArgumentParser()
parser.add_argument('mother_folder', type=str, help='A file to print')
args = parser.parse_args()

rename_folder(args.mother_folder)