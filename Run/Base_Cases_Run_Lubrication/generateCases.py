import math
import os
import glob
import linecache

parameters = [[1100, 0.7, 2000, 0.0020940, 1069.5], [1100, 0.7, 2000, 0.0068559, 1139.3], 
	      [1100, 0.7, 2000, 0.041295, 1202.4]]

variables = ['_um_', '_percent_', '_RPM_', '_dyn_viscosity_', '_mixture_density']

# case names (x2) and restart file names for the respective case
stableCaseNames = []
caseNames = []
restartFileNames = []
for i in range(len(parameters)):
	stableCaseNames.append('case_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+str(parameters[i][2])+variables[2]+str(parameters[i][3])+variables[3]+str(parameters[i][4])+variables[4])
	
	caseNames.append('run_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+str(parameters[i][2])+variables[2]+str(parameters[i][3])+variables[3]+str(parameters[i][4])+variables[4])
	
	restartFileNames.append('liggghts.restartCFDEM_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+str(parameters[i][2])+variables[2]+str(parameters[i][3])+variables[3]+str(parameters[i][4])+variables[4])

for k in range(len(caseNames)):
	c_dir = os.getcwd()
	MakeCases = os.path.join(c_dir,"MakeCases.sh")
	MakeCasesRenamed = os.path.join(c_dir,"MakeCases_tmp.sh")
	os.rename(MakeCases, MakeCasesRenamed)

	with open(MakeCasesRenamed, 'r') as inputFile, open(MakeCases, 'w') as outputFile:
		for line in inputFile:
			if 'caseName=' in line:
				outputFile.write('caseName='+caseNames[k]+'\n')
			elif 'stableCaseName=' in line:
				outputFile.write('stableCaseName='+stableCaseNames[k]+'\n')
			elif 'restartFile=' in line:
				outputFile.write('restartFile='+restartFileNames[k]+'\n')
			else:
				outputFile.write(line)
	outputFile.close()
	inputFile.close()
	os.remove(MakeCasesRenamed)
	#execute the bashScript
	os.system('chmod a+x MakeCases.sh')
	os.system('./MakeCases.sh')
