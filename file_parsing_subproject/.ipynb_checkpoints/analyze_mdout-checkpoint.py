import os.path
import argparse


if __name__== "__main__":

    ## Get the arguments.
    parser = argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy.")
    parser.add_argument("path", help="The filepath for the .mdout file to analyze.")

    args = parser.parse_args()

    ## Parse selected file and write Etot in a new file.

    with open(args.path, 'r') as outfile:
        data = outfile.readlines()

    etot_values=[]

    for line in data:
        if 'Etot' in line:
            line_to_words = line.split()
            Etot = line_to_words[2]
            etot_values.append(Etot)

    base_filename=os.path.basename(args.path).split('.')[0]
    output_filename=os.path.join(os.path.dirname(args.path), '{}_Etot.txt'.format(base_filename))

    with open(output_filename, 'w+') as datafile:
        for etot in etot_values[:-2]:
            datafile.write(F'{etot}\n')

