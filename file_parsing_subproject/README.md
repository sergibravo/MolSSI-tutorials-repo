
File parser (file_parsing_subproject): 

Scripts to open one or several .mdout files and parse the Etot values. An additional script to, furthermore, plot these values.

The folder contains the 3 main scripts:
- analyze_mdout: To parse one single file.
- analyze_mdouts: To parse several files with a .mdout extension
- analyze_plot_mdouts: To parse several files AND includes -plot argument to plot the Etot values in each time step. (It is redundant with previous script).


The mdout folder contains .mdout files to test the script. Also the .txt and .png files resulting from running the script.

The "3_Processing multiple files exercise" is an additional exercise. It contains a Jupyter Notebook that allows to parse several outfiles (.out files) to get their Etot in a single.txt document (energies.txt).