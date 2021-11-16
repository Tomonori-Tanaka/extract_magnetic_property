import argparse
import os
import re
import shutil
import subprocess

import numpy as np


parser = argparse.ArgumentParser(description='automation program for c/a from bcc to fcc')

phelp = 'initial value of c/a'
parser.add_argument('initial_c_a', type=float, help=phelp)

phelp = 'end value of c/a'
parser.add_argument('end_c_a', type=float, help=phelp)

phelp = 'division number'
parser.add_argument('division_num', type=int, help=phelp)

phelp = 'go keyword for sub dirctory'
parser.add_argument('go_keyword', help=phelp)

args = parser.parse_args()

c_over_a_ndarray = np.linspace(args.initial_c_a, args.end_c_a, args.division_num, endpoint=True)

current_path = os.getcwd()

for c_over_a in c_over_a_ndarray:
    c_over_a = round(c_over_a, 1)
    str_c_over_a = "{0:.1f}".format(c_over_a)
    subdir_path = current_path + "/" + str_c_over_a + "/" + args.go_keyword
    subprocess.call(['./submit.sh', subdir_path])

