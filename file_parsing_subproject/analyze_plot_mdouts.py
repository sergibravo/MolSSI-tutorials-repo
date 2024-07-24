import os.path
import argparse
import glob
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Get the arguments.
    parser = argparse.ArgumentParser(description="This script parses amber mdout files to extract the total energy.")
    parser.add_argument("path", help="The filepath for the .mdout file to analyze.")
    parser.add_argument("-plot", help="Plots Etot and saves image as file", action="store_true")

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
                    Etot = float(line_to_words[2])
                    etot_values.append(Etot)

        base_filename = os.path.basename(file_path).split('.')[0]
        output_filename = os.path.join(os.path.dirname(file_path), '{}_Etot.txt'.format(base_filename))

        with open(output_filename, 'w+') as datafile:
            for etot in etot_values[:-2]:
                datafile.write(F'{etot}\n')
        # Plot Etot
        if args.plot:
            plt.figure(figsize=(10, 6))
            plt.plot(etot_values, marker='o', linestyle='-')
            plt.xlabel('Timestep')
            plt.ylabel('Total Energy (Etot)')
            plt.title('Total Energy Over Time')
            plt.grid(True)  # Add grid lines for better readability
            plt.tight_layout() # Adjust layout for better fit

            # Customize Y-axis ticks for better readability
            plt.yticks(rotation=45)
            plt.xticks(rotation=45)

            plot_output_filename = os.path.join(os.path.dirname(file_path), '{}_Etot.png'.format(base_filename))
            plt.savefig(plot_output_filename)
            plt.close()  # Close the plot to avoid memory issues with multiple plots
