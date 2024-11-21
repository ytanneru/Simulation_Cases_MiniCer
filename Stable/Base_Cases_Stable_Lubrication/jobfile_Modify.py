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

for k in range(len(caseNames)):
	c_dir = os.getcwd()
	FolderPath = c_dir+'/'+caseNames[k]
	
	jobFile = os.path.join(FolderPath, "run_stable.job")
	jobFileRenamed = os.path.join(FolderPath, "run_stable.job_tmp")
	os.rename(jobFile, jobFileRenamed)
	with open(jobFileRenamed, 'r') as inputFile, open(jobFile, 'w') as outputFile:
		for line in inputFile:
			if '#SBATCH --partition=' in line:
				outputFile.write('#SBATCH --partition=standard'+'\n')
			elif '#SBATCH --time=' in line:
				outputFile.write('#SBATCH --time=7-00:00:00'+'\n')
			elif '#SBATCH --nodes=' in line:
				outputFile.write('#SBATCH --nodes=1'+'\n')
			elif '#SBATCH --job-name=' in line:
				outputFile.write('#SBATCH --job-name='+caseNames[k]+'\n')
			elif '#SBATCH --ntasks-per-node=' in line:
				outputFile.write('#SBATCH --ntasks-per-node=20'+'\n')
			#elif 'working_dir=' in line:
			#	outputFile.write('working_dir='+FolderPath+'\n')	
			else:
				outputFile.write(line)
	outputFile.close()
	inputFile.close()
	os.remove(jobFileRenamed)



