import math
import os
import glob
import linecache

parameters = [[1100, 0.7, 2000, 0.0020940, 1069.5], [1100, 0.7, 2000, 0.0068559, 1139.3], 
	      [1100, 0.7, 2000, 0.041295, 1202.4]]

variables = ['_um_', '_percent_', '_RPM_', '_dyn_viscosity_', '_mixture_density']

# case names
caseNames = []
for i in range(len(parameters)):
	caseNames.append('run_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+str(parameters[i][2])+variables[2]+str(parameters[i][3])+variables[3]+str(parameters[i][4])+variables[4])

home_dir = os.getcwd()
for i in range(len(caseNames)):
	cur_dir = home_dir
	os.chdir(cur_dir)
	run_dir = cur_dir+'/'+caseNames[i]
	os.chdir(run_dir)
	os.system('mkdir postProcessEnergies')
	post_dir = run_dir+'/postProcessEnergies'
	os.chdir(post_dir)
	os.system('cp ../../Stress_Energy_Calculation.py .')
	
c_dir = home_dir
for k in range(len(caseNames)):
	os.chdir(c_dir)
	FolderPath = c_dir+'/'+caseNames[k]+'/postProcessEnergies'
	os.chdir(FolderPath)
	#print(os.getcwd())
	print('Running post-processing in '+caseNames[k]+' ...'+'\n')
	os.system('python3 Stress_Energy_Calculation.py')
