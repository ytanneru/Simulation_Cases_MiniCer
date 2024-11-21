import math
import os
import glob
import linecache

# Importing files
path = os.getcwd()
files_path_DEM = path+'/DEM/post/torque.txt' # Where the files are located
#files_path_DEM = 'torque.txt'
files_path_CFD = path+'/CFD/logForces_Stirrer.stl' # Where the files are located
#files_path_CFD = 'logForces_Stirrer.stl'
save_path = path # Where to save the extracted files ?

CFD_torque = []
# CFD torque
with open(files_path_CFD, 'r') as inputFile:
    next(inputFile)
    for lines in inputFile:
        data = lines.split(" ")
        CFD_torque_x = float(data[4])
        CFD_torque_y = float(data[5])
        CFD_torque_z = float(data[6])
        CFD_torque.append(math.sqrt((CFD_torque_x*CFD_torque_x)+(CFD_torque_y*CFD_torque_y)+(CFD_torque_z*CFD_torque_z)))

inputFile.close()

Average_CFD_torque = sum(CFD_torque)/len(CFD_torque) # for one rotation
 
#print("Average CFD torque =", round(Average_CFD_torque, 2))

DEM_torque = []
# DEM torque
with open(files_path_DEM, 'r') as inputFile:
    next(inputFile)
    for lines in inputFile:
        data = lines.split(" ")
        DEM_torque_x = float(data[1])
        DEM_torque_y = float(data[2])
        DEM_torque_z = float(data[3])
        DEM_torque.append(math.sqrt((DEM_torque_x*DEM_torque_x)+(DEM_torque_y*DEM_torque_y)+(DEM_torque_z*DEM_torque_z)))

inputFile.close()

Average_DEM_torque = sum(DEM_torque)/len(DEM_torque) # for one rotation
 
#print("Average DEM torque =", round(Average_DEM_torque, 2))

#print("Total torque =", round(Average_CFD_torque + Average_DEM_torque,2))

# Write the data to different text files
stats = 'torque_data.txt'
if os.path.exists(stats):
    os.remove(stats)

with open(stats,'w') as f:
    f.write('Average CFD torque: '+str(Average_CFD_torque)+'\n')
    f.write('Average DEM torque: '+str(Average_DEM_torque)+'\n')
    f.write('Average Total Torque: '+str(Average_CFD_torque+Average_DEM_torque)+'\n')
    
f.close()
