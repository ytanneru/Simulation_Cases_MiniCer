import math
import os
import glob
import linecache

parameters = [[800, 0.8, 2000], [800, 0.8, 2500], [800, 0.8, 3000],
	      [800, 0.7, 2000], [800, 0.7, 2500], [800, 0.7, 3000],
	      [800, 0.6, 2000], [800, 0.6, 2500], [800, 0.6, 3000]]

variables = ['_um_', '_percent_', '_RPM']

# case names (x2) and restart file names for the respective case
stableCaseNames = []
caseNames = []
restartFileNames = []
for i in range(len(parameters)):
	stableCaseNames.append('case_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+str(parameters[i][2])+variables[2])
	
	caseNames.append('run_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+str(parameters[i][2])+variables[2])
	
	restartFileNames.append('liggghts.restartCFDEM_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+str(parameters[i][2])+variables[2])

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
