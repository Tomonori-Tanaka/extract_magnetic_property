import argparse
import os
import sys
from numpy import linspace

AFTER_DECIMAL_POINT_LATTICE_CONST_DIR = 2
AFTER_DECIMAL_POINT_ATOMIC_NUM_DIR = 1
EXTRACT_KEYWORD_TC = 'Tc (in mean field approximation)'

parser = argparse.ArgumentParser(description='Extract magnetic moment or Tc from the result of phonon version of '
                                             'AkaiKKR: lattice_const/atomic_number/output_file or '
                                             'lattice_const/atomic_number/tc/output_file')

help_text = 'start lattice constant (Angstrom)'
parser.add_argument('lattice_const_start', type=float, help=help_text)

help_text = 'end lattice constant (Angstrom)'
parser.add_argument('lattice_const_end', type=float, help=help_text)

help_text = 'division number (number of directory) of lattice constant'
parser.add_argument('division_num_lattice_const', type=int, help=help_text)

help_text = 'start atomic number'
parser.add_argument('atomic_number_start', type=float, help=help_text)

help_text = 'end atomic number'
parser.add_argument('atomic_number_end', type=float, help=help_text)

help_text = 'division number (number of directory) of atomic number'
parser.add_argument('division_num_atomic_num', type=int, help=help_text)

help_text = 'output file name of AkaiKKR'
parser.add_argument('output_file_name', help=help_text)

help_text = 'The number of the component of atomic displacements'
parser.add_argument('number_of_disp_component', help=help_text)

help_text = 'magnetic properties which will be extracted'
parser.add_argument('mag_property', choices=['tc', 'moment', 'j'], help=help_text)

args = parser.parse_args()

def return_path(*dir_names):
    """
    Return absolute path of the directory.
    :param dir_names: The names of hierarchies
    :return: absolute path of the directory
    """
    path = "/"
    for name in dir_names:
        path = path + name + "/"
    return path

# ----- main part -----
lattice_constants = linspace(args.lattice_const_start, args.lattice_const_end, args.division_num_lattice_const,
                             endpoint=True)
atomic_numbers = linspace(args.atomic_number_start, args.atomic_number_end, args.division_num_atomic_num,
                          endpoint=True)

path_root = os.getcwd()
for lattice_const in lattice_constants:
    for atomic_num in atomic_numbers:
        lattice_const_str = "%.*f" % (AFTER_DECIMAL_POINT_LATTICE_CONST_DIR, lattice_const)
        atomic_num = round(atomic_num, AFTER_DECIMAL_POINT_ATOMIC_NUM_DIR)
        atomic_num_str = "%.*f" % (AFTER_DECIMAL_POINT_ATOMIC_NUM_DIR, atomic_num)
        # get the absolute path of scf directory
        path_scf = return_path(path_root, lattice_const_str, atomic_num_str)
        path_destination = path_scf

        if args.mag_property == 'tc' or args.property == 'j':
            if os.path.exists(path_scf):
                pass
            else:
                sys.exit("!ERROR!: Parent directory (SCF directory) does not exist.")
            path_destination = return_path(path_root, lattice_const_str, atomic_num_str, args.mag_property)

        with open(f'{path_destination}{args.output_file_name}', mode='r', encoding='utf-8') as f:
            if args.mag_property == 'tc':
                for line in f:
                    if EXTRACT_KEYWORD_TC in line:
                        tc_value = line.split()[6]
                        tc_value = tc_value.replace("K", "")
                        print(tc_value)