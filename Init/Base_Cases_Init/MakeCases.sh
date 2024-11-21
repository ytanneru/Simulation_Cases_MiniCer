
caseName=case_1100_um_0.8_percent

masterPath="$PWD"

baseCasePath=$masterPath/Base_Case

mkdir $caseName

casePath="$masterPath/$caseName"

# General files
cp -r $baseCasePath/CAD $casePath
cp -r $baseCasePath/DEM $casePath
