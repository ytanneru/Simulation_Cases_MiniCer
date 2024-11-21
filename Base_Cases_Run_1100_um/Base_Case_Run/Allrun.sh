#!/bin/bash

#===================================================================#
# allrun script for testcase as part of test routine 
# run settlingTest
# Christoph Goniva - July. 2011, mod by Alice Hager - July 2011
#===================================================================#

source $CFDEM_PROJECT_DIR/etc/functions.sh #/etc/functions.sh

#- define variables
casePath="$PWD"

echo $casePath

# check if mesh was built
if [ -f "$casePath/CFD/constant/polyMesh/points" ]; then
    echo "mesh was built before - using old mesh"
else
    echo "mesh needs to be built"
    cd $casePath/CFD
    # cp /system/controlDict_CFD /system/controlDict
    cp $casePath/CFD/system/controlDict_CFDEM $casePath/CFD/system/controlDict
    # surfaceFeatureExtract
    blockMesh
    snappyHexMesh -overwrite
    decomposePar -copyZero
   
    # mpirun -np 4 $(getApplication)
    # blockMesh
fi

cp $casePath/CFD/system/controlDict_CFDEM $casePath/CFD/system/controlDict

#gnome-terminal --title='cfdemSolverIB twoSpheresGlowinskiMPI CFD' -e "bash $casePath/parCFDDEMrun.sh"
bash $casePath/parCFDDEMrun.sh
