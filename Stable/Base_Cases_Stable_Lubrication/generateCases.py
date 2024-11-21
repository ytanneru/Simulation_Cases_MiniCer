import math
import os
import glob
import linecache

parameters = [[1100, 0.7, 2000, 0.0020940, 1069.5], [1100, 0.7, 2000, 0.0068559, 1139.3], 
	      [1100, 0.7, 2000, 0.041295, 1202.4]]

variables = ['_um_', '_percent_', '_RPM_', '_dyn_viscosity_', '_mixture_density']

variables_restart = ['_um_', '_percent']

# case names
caseNames = []
for i in range(len(parameters)):
	caseNames.append('case_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+str(parameters[i][2])+variables[2]+str(parameters[i][3])+variables[3]+str(parameters[i][4])+variables[4])

# restart file names for the respective case
restartFileNames = []
for i in range(len(parameters)):
	restartFileNames.append('liggghts.restart_'+str(parameters[i][0])+variables_restart[0]+str(parameters[i][1])+variables_restart[1])

for k in range(len(caseNames)):
	c_dir = os.getcwd()
	MakeCases = os.path.join(c_dir,"MakeCases.sh")
	MakeCasesRenamed = os.path.join(c_dir,"MakeCases_tmp.sh")
	os.rename(MakeCases, MakeCasesRenamed)

	with open(MakeCasesRenamed, 'r') as inputFile, open(MakeCases, 'w') as outputFile:
		for line in inputFile:
			if 'caseName=' in line:
				outputFile.write('caseName='+caseNames[k]+'\n')
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
	





