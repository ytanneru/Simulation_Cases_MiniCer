import math
import os
import glob
import linecache

parameters = [[800, 0.6], [1100, 0.6], [800, 0.7], [1100, 0.7], [800, 0.8], [1100, 0.8] ]

variables = ['_um_', '_percent']

# case names
caseNames = []
for i in range(len(parameters)):
	caseNames.append('case_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1])

for k in range(len(caseNames)):
	c_dir = os.getcwd()
	MakeCases = os.path.join(c_dir,"MakeCases.sh")
	MakeCasesRenamed = os.path.join(c_dir,"MakeCases_tmp.sh")
	os.rename(MakeCases, MakeCasesRenamed)

	with open(MakeCasesRenamed, 'r') as inputFile, open(MakeCases, 'w') as outputFile:
		for line in inputFile:
			if 'caseName=' in line:
				outputFile.write('caseName='+caseNames[k]+'\n')
			else:
				outputFile.write(line)
	outputFile.close()
	inputFile.close()
	os.remove(MakeCasesRenamed)
	#execute the bashScript
	os.system('chmod a+x MakeCases.sh')
	os.system('./MakeCases.sh')
	





