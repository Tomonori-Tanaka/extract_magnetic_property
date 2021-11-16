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

args = parser.parse_args()

c_over_a_ndarray = np.linspace(args.initial_c_a, args.end_c_a, args.division_num, endpoint=True)

for c_over_a in c_over_a_ndarray:
    c_over_a = round(c_over_a, 1)
    subprocess.call(['./submit.sh','{0:.1f}'.format(c_over_a)])

