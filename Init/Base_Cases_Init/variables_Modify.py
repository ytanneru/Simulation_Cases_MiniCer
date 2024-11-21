import math
import os
import glob
import linecache

parameters = [[800, 0.6], [1100, 0.6], [800, 0.7], [1100, 0.7], [800, 0.8], [1100, 0.8] ]

variables = ['_um_', '_percent']

# patricle_dia_mm = ['0.800e-3', '1.1e-3']

# case names
caseNames = []
for i in range(len(parameters)):
	caseNames.append('case_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1])


for k in range(len(caseNames)):
	c_dir = os.getcwd()
	FolderPath = c_dir+'/'+caseNames[k]
	DEMPath = FolderPath+'/'+'DEM'
	
	# dataHeadDEM
	dataHeadDEM = os.path.join(DEMPath, "dataHeadDEM")
	dataHeadDEMRenamed = os.path.join(DEMPath, "dataHeadDEM_tmp")
	os.rename(dataHeadDEM, dataHeadDEMRenamed)
	with open(dataHeadDEMRenamed, 'r') as inputFile, open(dataHeadDEM, 'w') as outputFile:
		for line in inputFile:
			if 'variable dia_zirc_um' in line:
				outputFile.write('variable dia_zirc_um	equal '+str(parameters[k][0])+'\n')
			elif 'variable fillingDegree' in line:
				outputFile.write('variable fillingDegree	equal  '+str(parameters[k][1])+'\n')					
			else:
				outputFile.write(line)
	outputFile.close()
	inputFile.close()
	os.remove(dataHeadDEMRenamed)
	
	# in.liggghts_init
	in_liggghts_init = os.path.join(DEMPath, "in.liggghts_init")
	in_liggghts_initRenamed = os.path.join(DEMPath, "in_liggghts_init_tmp")
	os.rename(in_liggghts_init, in_liggghts_initRenamed)
	with open(in_liggghts_initRenamed, 'r') as inputFile, open(in_liggghts_init, 'w') as outputFile:
		for line in inputFile:
			if 'write_restart' in line:
				outputFile.write('write_restart   post/restart/liggghts.restart_'+str(parameters[k][0])+variables[0]+str(parameters[k][1])+variables[1]+'\n')
				# print('write_restart   post/restart/liggghts.restart_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+'\n')	
			else:
				outputFile.write(line)
	outputFile.close()
	inputFile.close()
	os.remove(in_liggghts_initRenamed)
	
