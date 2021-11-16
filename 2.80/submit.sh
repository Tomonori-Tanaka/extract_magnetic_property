#!/bin/bash
c_over_a=$1

cd $c_over_a
pjsub job.sh
cd $SCRIPT_DIR
