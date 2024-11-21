import math
import os
import glob
import linecache

parameters = [[800, 0.8, 2000], [800, 0.8, 2500], [800, 0.8, 3000],
	      [800, 0.7, 2000], [800, 0.7, 2500], [800, 0.7, 3000],
	      [800, 0.6, 2000], [800, 0.6, 2500], [800, 0.6, 3000],
	      [1100, 0.8, 2000], [1100, 0.8, 2500], [1100, 0.8, 3000],
	      [1100, 0.7, 2000], [1100, 0.7, 2500], [1100, 0.7, 3000],
	      [1100, 0.6, 2000], [1100, 0.6, 2500], [1100, 0.6, 3000]]

variables = ['_um_', '_percent_', '_RPM']

variables_restart = ['_um_', '_percent']

# case names
caseNames = []
for i in range(len(parameters)):
	caseNames.append('case_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+str(parameters[i][2])+variables[2])

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
	





