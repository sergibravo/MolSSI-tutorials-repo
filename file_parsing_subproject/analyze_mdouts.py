import os.path
import argparse
import glob

if __name__ == "__main__":

    # Get the arguments.
    parser = argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy.")
    parser.add_argument("path", help="The filepath for the .mdout file to analyze.")

    args = parser.parse_args()

    # Use glob to match files (to make it work in all operating systems):
    file_paths = glob.glob(args.path)

    for file_path in file_paths:
        # Parse selected file and write Etot in a new file.
        with open(file_path, 'r') as outfile:
            data = outfile.readlines()

            etot_values = []

            for line in data:
                if 'Etot' in line:
                    line_to_words = line.split()
                    Etot = line_to_words[2]
                    etot_values.append(Etot)

            base_filename = os.path.basename(file_path).split('.')[0]
            output_filename = os.path.join(os.path.dirname(file_path), '{}_Etot.txt'.format(base_filename))

            with open(output_filename, 'w+') as datafile:
                for etot in etot_values[:-2]:
                    datafile.write(F'{etot}\n')
