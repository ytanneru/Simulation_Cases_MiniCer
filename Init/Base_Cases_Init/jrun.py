import math
import os
import glob
import linecache
import time

parameters = [[800, 0.6], [1100, 0.6], [800, 0.7], [1100, 0.7], [800, 0.8], [1100, 0.8] ]

variables = ['_um_', '_percent']

# patricle_dia_mm = ['0.800e-3', '1.1e-3']

# case names
caseNames = []
for i in range(len(parameters)):
	caseNames.append('case_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1])

c_dir = os.getcwd()
for k in range(len(caseNames)):
	os.chdir(c_dir)
	FolderPath = c_dir+'/'+caseNames[k]
	DEMPath = FolderPath+'/'+'DEM'
	os.chdir(DEMPath)
	#print(os.getcwd())
	os.system('chmod a+x run_init.job')
	os.system('sbatch run_init.job')
	time.sleep(3) # Sleep for 3 seconds



