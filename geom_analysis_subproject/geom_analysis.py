"""
This module has functions associated with analyzing the geometry of a molecule.

When run as a script and given an xyz file, this script will print out the bonds.

Run $ python geom_analysis.py --help to see input options.
"""

# Import necessary libraries.

import numpy
import os
import argparse


# Define funcions

# Function: Calculate distance between 2 given atoms.


def calculate_distance(atom1_coord, atom2_coord):
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    bond_length_12 = numpy.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
    return bond_length_12


# Decide if a given distance between 2 atoms falls into the 'bond' category.


def bond_check(atom_distance, minimum_length=0, maximum_length=1.5):
    if atom_distance < 0:
        raise ValueError(f'Invalid atom distance {atom_distance}. Distance cannot be less than 0!')
    if minimum_length < atom_distance <= maximum_length:
        return True
    else:
        return False


# Given the filepath to an .xyf file, the function opens it.


def open_xyz(filename):
    fpath, extension = os.path.splitext(filename)

    if extension.lower() != '.xyz':
        raise ValueError(f'Invalid file extension. Please provide a .xyz file')

    xyz_file = numpy.genfromtxt(fname=filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:, 0]
    coord = (xyz_file[:, 1:])
    coord = coord.astype(float)
    return symbols, coord


# Given an xyz file, this script will print out the bonds.
if __name__ == "__main__":

    # Get the arguments.

    parser = argparse.ArgumentParser(
        description="This script analyzes a user given xyz file and outputs the length of the bonds.")
    parser.add_argument("xyz_file", help="The filepath for the xyz file to analyze.")
    parser.add_argument('-minimum_length', help='The minimum distance to consider atoms bonded.', type=float, default=0)
    parser.add_argument('-maximum_length', help='The maximium distance to consider atoms bonded.', type=float,
                        default=1.5)

    args = parser.parse_args()

    symbols, coord = open_xyz(args.xyz_file)
    num_atoms = len(symbols)

    for num1 in range(0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1 < num2:
                bond_length_12 = calculate_distance(coord[num1], coord[num2])
                if bond_check(bond_length_12, minimum_length=args.minimum_length,
                              maximum_length=args.maximum_length) is True:
                    print(F'{symbols[num1]} to {symbols[num2]} : {bond_length_12:.3f}')