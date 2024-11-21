caseName=run_1100_um_0.6_percent_3000_RPM
stableCaseName=case_1100_um_0.6_percent_3000_RPM
restartFile=liggghts.restartCFDEM_1100_um_0.6_percent_3000_RPM


masterPath="$PWD"

baseCasePath=$masterPath/Base_Case_Run


mkdir $caseName

casePath="$masterPath/$caseName"
stableCasePath="$masterPath/$stableCaseName"
cfdPath=$casePath/CFD
cfdPathStable=$stableCasePath/CFD
demPath=$casePath/DEM
demPathStable=$stableCasePath/DEM

# General files
cp -r $baseCasePath/CAD $casePath
cp -r $baseCasePath/DEM $casePath
cp -r $baseCasePath/CFD $casePath
cp $baseCasePath/Allrun.sh $casePath
cp $baseCasePath/parCFDDEMrun.sh $casePath

# reconstruct the latest (CFD) time from stable case and copy it to the current case in CFD 
cd $cfdPathStable
if [ -f "$cfdPathStable/0.*/U" ]; then
    echo "Already Exists!"
    cp -r $cfdPathStable/0.* $cfdPath
else
    echo "Need to reconstruct!"
    reconstructPar -noLagrangian -latestTime
    cp -r $cfdPathStable/0.* $cfdPath
fi

cd $masterPath

# Job file
cp -r $baseCasePath/run_final.job $casePath

# Restart file
cp -r $baseCasePath/Restart/$restartFile $casePath/DEM/post/restart

