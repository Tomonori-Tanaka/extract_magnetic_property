import argparse
import os
import re
import shutil

import numpy as np

parser = argparse.ArgumentParser(description='automation program for c/a from bcc to fcc')

phelp = 'initial lattice constant'
parser.add_argument('a_init', type=float, help=phelp)

phelp = 'end lattice constant '
parser.add_argument('a_end', type=float, help=phelp)

phelp = 'division number'
parser.add_argument('division_num', type=int, help=phelp)

phelp = 'input kkr file'
parser.add_argument('input_file', help=phelp)

args = parser.parse_args()

lc_ndarray = np.linspace(args.a_init, args.a_end, args.division_num, endpoint=True)

for lc in lc_ndarray:
    with open(args.input_file, encoding='utf-8') as f:
        lc = round(lc, 1)
        body = f.read()
        body = re.sub('XXX', str(lc), body)
    try:
        os.mkdir('{0:.1f}'.format(lc))
    except:
        print('{0:.1f} directory already exists. We skip it.'.format(lc))
        continue
    with open('tmp.dat', mode='w', encoding='utf-8') as f:
        f.write(body)
    shutil.move('./tmp.dat', './{0:.1f}/kkrin.dat'.format(lc))
    shutil.copy('./job.sh', './{0:.1f}/'.format(lc))

