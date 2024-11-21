
#!/bin/bash

#===================================================================#
# allrun script for testcase as part of test routine
# run settlingTest CFD part
# Christoph Goniva - Feb. 2011
#===================================================================#

#- source CFDEM env vars
. ~/.bashrc

#- include functions
source  $CFDEM_PROJECT_DIR/etc/functions.sh

#--------------------------------------------------------------------------------#
#- define variables
casePath="$PWD"
logpath=$casePath
headerText="run_parallel_cfdemSolverPiso_IBg_CFDDEM"
logfileName="log_$headerText"
solverName="cfdemSolverPisoIBg"
nrProcs="4"
machineFileName="none"   # yourMachinefileName | none
debugMode="off"          # on | off| strict
reconstructCase="false"  # true | false
testHarnessPath="$CFDEM_TEST_HARNESS_PATH"
runPython="false"
postproc="false"
#--------------------------------------------------------------------------------#

#- call function to run a parallel CFD-DEM case
parCFDDEMrun $logpath $logfileName $casePath $headerText $solverName $nrProcs $machineFileName $debugMode

#- case needs special reconstruction
if [ $reconstructCase == "true" ]
  then
    cd $casePath/CFD
    reconstructParMesh -mergeTol 1e-06
    reconstructPar -noLagrangian
fi

if [ $runPython == "true" ]
  then

    cd $casePath/PostProc
    python postproc.py
fi

if [ $postproc == "true" ]
  then
    #- get VTK data from CFD sim
    cd $casePath/CFD
    foamToVTK
fi



