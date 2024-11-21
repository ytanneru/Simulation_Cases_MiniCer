caseName=case_1100_um_0.6_percent_3000_RPM
restartFile=liggghts.restart_1100_um_0.6_percent

masterPath="$PWD"

baseCasePath=$masterPath/Base_Case_Stable

mkdir $caseName

casePath="$masterPath/$caseName"
cfdPath="$casePath/$CFD"
demPath="$casePath/$DEM"

# General files
cp -r $baseCasePath/CAD $casePath
cp -r $baseCasePath/DEM $casePath
cp -r $baseCasePath/CFD $casePath
cp $baseCasePath/Allrun.sh $casePath
cp $baseCasePath/parCFDDEMrun.sh $casePath

# Job file
cp -r $baseCasePath/run_stable.job $casePath

# Restart file
cp -r $baseCasePath/Restart/$restartFile $casePath/DEM/post/restart


