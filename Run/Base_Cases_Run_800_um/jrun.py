import math
import os
import glob
import linecache
import time

parameters = [[800, 0.8, 2000], [800, 0.8, 2500], [800, 0.8, 3000],
	      [800, 0.7, 2000], [800, 0.7, 2500], [800, 0.7, 3000],
	      [800, 0.6, 2000], [800, 0.6, 2500], [800, 0.6, 3000],
	      [1100, 0.8, 2000], [1100, 0.8, 2500], [1100, 0.8, 3000],
	      [1100, 0.7, 2000], [1100, 0.7, 2500], [1100, 0.7, 3000],
	      [1100, 0.6, 2000], [1100, 0.6, 2500], [1100, 0.6, 3000]]

variables = ['_um_', '_percent_', '_RPM']


# case names
caseNames = []
for i in range(len(parameters)):
	caseNames.append('case_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+str(parameters[i][2])+variables[2])

c_dir = os.getcwd()
for k in range(len(caseNames)):
	os.chdir(c_dir)
	FolderPath = c_dir+'/'+caseNames[k]
	os.chdir(FolderPath)
	#print(os.getcwd())
	os.system('chmod a+x run_stable.job')
	os.system('sbatch run_stable.job')
	time.sleep(3) # Sleep for 3 seconds



