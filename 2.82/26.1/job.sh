#!/bin/bash
#PJM -L "node=1"               # the number of nodes
#PJM -L "rscgrp=small"         # specification of resource group
#PJM -L "elapse=7:00:00"         # walltime
#PJM -S                        # whether output statistical information or not
#PJM --name Fe300k

#. /vol0004/apps/oss/spack/share/spack/setup-env.sh
#spack load  quantum-espresso@6.6

export OMP_NUM_THREADS=20

# execute job
#pw.x < graphene.in > graphene.scf.out
#kkrph_mse_dos1_j3 < kkrin.dat > output.dat
#kkrph_mse_dos1_j3 < dosin.dat > dosout.dat
kkrph_mse65_dos080_j6 < kkrin.dat > output.dat
#kkrph_mse65_dos080_j3 < dosin.dat > dosout.dat
#gpd dosout.dat
