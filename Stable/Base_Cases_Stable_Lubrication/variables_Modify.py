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
	
# variables and calculations for respective cases
number_of_rotations = 2

startTimes = []
endTimes = []
smoothingLengths = []
writeIntervals = []
rotorSpeeds = []
viscosities_dyn = []
densities_mix = []
viscosities_kin = []
for i in range(len(parameters)):
	# start and end times
	startTime = 0.
	startTimes.append(startTime)
	endTime = number_of_rotations*(60.0/parameters[i][2])
	endTimes.append(endTime)
	
	# smoothing length
	particleSize_meters = parameters[i][0]/(1e6)
	smoothingLength = round(3.0*particleSize_meters,9)
	smoothingLengths.append(smoothingLength)

	# write interval (20 files per simulation)
	runTime = round(endTime-startTime,9)
	writeInterval = round((runTime*(1/20)),9);
	writeIntervals.append(writeInterval)
	
	# rotor speed
	rotorSpeeds.append(parameters[i][2])
	
	# viscosity and density
	visc_dyn = round(parameters[i][3],9)
	dens_mix = round(parameters[i][4],9)
	visc_kin = round(visc_dyn/dens_mix,10)
	viscosities_dyn.append(visc_dyn)
	densities_mix.append(dens_mix)
	viscosities_kin.append(visc_kin)
	
	# torque frequency (not necessary for stable)

## Modifying the variables
for k in range(len(caseNames)):
	c_dir = os.getcwd()
	FolderPath = c_dir+'/'+caseNames[k]
	CFDPath = FolderPath+'/'+'CFD'
	constantPath = CFDPath+'/'+'constant'
	systemPath = CFDPath+'/'+'system'
	DEMPath = FolderPath+'/'+'DEM'
	
	# dataHeadCFDEM
	dataHeadCFDEM = os.path.join(DEMPath, "dataHeadCFDEM")
	dataHeadCFDEMRenamed = os.path.join(DEMPath, "dataHeadCFDEM_tmp")
	os.rename(dataHeadCFDEM, dataHeadCFDEMRenamed)
	with open(dataHeadCFDEMRenamed, 'r') as inputFile, open(dataHeadCFDEM, 'w') as outputFile:
		for line in inputFile:
			if 'variable dia_zirc_um' in line:
				outputFile.write('variable dia_zirc_um	equal '+str(parameters[k][0])+'\n')
			elif 'variable fillingDegree' in line:
				outputFile.write('variable fillingDegree	equal  '+str(parameters[k][1])+'\n')
			elif 'variable rotorSpeed' in line:
				outputFile.write('variable rotorSpeed	equal '+str(parameters[k][2])+'\n')
			elif 'variable number_of_rot' in line:
				outputFile.write('variable number_of_rot	equal  '+str(number_of_rotations)+'\n')
			elif 'variable viscosity' in line:
				outputFile.write('variable viscosity	equal  '+str(viscosities_dyn[k])+'\n')					
			else:
				outputFile.write(line)
	outputFile.close()
	inputFile.close()
	os.remove(dataHeadCFDEMRenamed)
	
	# in.liggghts_cfd
	in_liggghts_cfd = os.path.join(DEMPath, "in.liggghts_cfd")
	in_liggghts_cfdRenamed = os.path.join(DEMPath, "in_liggghts_cfd_tmp")
	os.rename(in_liggghts_cfd, in_liggghts_cfdRenamed)
	with open(in_liggghts_cfdRenamed, 'r') as inputFile, open(in_liggghts_cfd, 'w') as outputFile:
		for line in inputFile:
			if 'read_restart' in line:
				outputFile.write('read_restart   ../DEM/post/restart/liggghts.restart_'+str(parameters[k][0])+variables_restart[0]+str(parameters[k][1])+variables_restart[1]+'\n')
				# print('write_restart   post/restart/liggghts.restart_'+str(parameters[i][0])+variables[0]+str(parameters[i][1])+variables[1]+'\n')	
			else:
				outputFile.write(line)
	outputFile.close()
	inputFile.close()
	os.remove(in_liggghts_cfdRenamed)
	
	# dataCFD
	dataHeadCFD = os.path.join(constantPath, "dataHeadCFD")
	dataHeadCFDRenamed = os.path.join(constantPath, "dataHeadCFD_tmp")
	os.rename(dataHeadCFD, dataHeadCFDRenamed)
	with open(dataHeadCFDRenamed, 'r') as inputFile, open(dataHeadCFD, 'w') as outputFile:
		for line in inputFile:
			if 'startTimee' in line:
				outputFile.write('startTimee '+str(startTimes[k])+';'+'\n')
			elif 'endTimee' in line:
				outputFile.write('endTimee '+str(endTimes[k])+';'+'\n')
			elif 'writeIntervall' in line:
				outputFile.write('writeIntervall '+str(writeIntervals[k])+';'+'\n')
			elif 'smoothingLengthL' in line:
				outputFile.write('smoothingLengthL '+str(smoothingLengths[k])+';'+'\n')
			elif 'rotorSpeed' in line:
				outputFile.write('rotorSpeed '+str(rotorSpeeds[k])+';'+'\n')
			elif 'viscosityFl' in line:
				outputFile.write('viscosityFl '+str(viscosities_kin[k])+';'+'\n')
			elif 'densityFl' in line:
				outputFile.write('densityFl '+str(densities_mix[k])+';'+'\n')			
			else:
				outputFile.write(line)
	outputFile.close()
	inputFile.close()
	os.remove(dataHeadCFDRenamed)
	
	# liggghtsCommands
	liggghtsCommands = os.path.join(constantPath, "liggghtsCommands")
	liggghtsCommandsRenamed = os.path.join(constantPath, "liggghtsCommands_tmp")
	os.rename(liggghtsCommands, liggghtsCommandsRenamed)
	with open(liggghtsCommandsRenamed, 'r') as inputFile, open(liggghtsCommands, 'w') as outputFile:
		for line in inputFile:
			if 'writeName' in line:
				outputFile.write('    writeName "post/restart/liggghts.restartCFDEM_'+str(parameters[k][0])+variables[0]+str(parameters[k][1])+variables[1]+str(parameters[k][2])+variables[2]+str(parameters[k][3])+variables[3]+str(parameters[k][4])+variables[4]+'";'+'\n')
				#print('	writeName "post/restart/liggghts.restartCFDEM_'+str(parameters[k][0])+variables[0]+str(parameters[k][1])+variables[1]+str(parameters[k][2])+variables[2]+'";'+'\n')
			else:
				outputFile.write(line)
	outputFile.close()
	inputFile.close()
	os.remove(liggghtsCommandsRenamed)
	
	
	
