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
	
	
	jobFile = os.path.join(DEMPath, "run_init.job")
	jobFileRenamed = os.path.join(FolderPath, "run_init.job_tmp")
	os.rename(jobFile, jobFileRenamed)
	with open(jobFileRenamed, 'r') as inputFile, open(jobFile, 'w') as outputFile:
		for line in inputFile:
			if '#SBATCH --partition=' in line:
				outputFile.write('#SBATCH --partition=shortrun_small'+'\n')
			elif '#SBATCH --time=' in line:
				outputFile.write('#SBATCH --time=2-12:00:00'+'\n')
			elif '#SBATCH --nodes=' in line:
				outputFile.write('#SBATCH --nodes=1'+'\n')
			elif '#SBATCH --job-name=' in line:
				outputFile.write('#SBATCH --job-name='+caseNames[k]+'\n')
			elif '#SBATCH --ntasks-per-node=' in line:
				outputFile.write('#SBATCH --ntasks-per-node=16'+'\n')
			#elif 'working_dir=' in line:
			#	outputFile.write('working_dir='+FolderPath+'\n')	
			else:
				outputFile.write(line)
	outputFile.close()
	inputFile.close()
	os.remove(jobFileRenamed)



