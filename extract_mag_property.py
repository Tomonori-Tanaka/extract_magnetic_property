import argparse

parser = argparse.ArgumentParser(description='Extract magnetic properties from the result of phonon version of AkaiKKR:'
                                             '  lattice_const/atomic_number/output_file')

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

help_text = 'subdirectory name. Keyword is restricted to "tc" or "j" in the current version.'
parser.add_argument('-sub', '--subdir_name', choices=['tc', 'j'], help=help_text)

args = parser.parse_args()