#experience to learn "argparse" library
import argparse

#pratice code for argparse module
def print_file(word):
    file1 = open("MyFile.txt","w")
    file1.write(word)
    file1.close()

parser = argparse.ArgumentParser()
parser.add_argument('word', type=str, help='A word to print')
args = parser.parse_args()

print_file(args.word)