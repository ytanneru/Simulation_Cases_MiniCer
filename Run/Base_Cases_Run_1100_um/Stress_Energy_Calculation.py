import fileinput
import time
import math
import numpy as np
#import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
#from tkinter import *
#import statistics

start = time.time()

# Importing files
path = os.getcwd()
files_path = path+'/../CFD' # Where the files are located
save_path = path # Where to save the extracted files ?
rotor_files = []
wall_files = []
bead_files = []
for i in os.listdir(files_path):
    #if os.path.isfile(os.path.join(files_path,i))  and 'Rotor_Wandkontakte_' in i:
    if i.startswith("Rotor_Wandkontakte_"):
        rotor_files.append(i)
    #if os.path.isfile(os.path.join(files_path,i))  and 'Wandkontakte_' in i:
    if i.startswith("Wandkontakte_"):
        wall_files.append(i)
    #if os.path.isfile(os.path.join(files_path,i))  and 'Kugelkontakte_' in i:
    if i.startswith("Kugelkontakte_"):
        bead_files.append(i)

types = ["rotor", "wall", "bead"]
# Start to iterate over different files and syve information
k = 0
for iii in [rotor_files, wall_files, bead_files]:
    faulty_contacts = 0 # Total number of faulty contacts among all the modes
    faulty_contacts_unique = 0 # Total number of faulty contacts for each unique collision (generally should stay zero)
    contacts_tra_norm  = 0 # Total number of trans. normal contacts
    contacts_rot_norm  = 0 # Total number of rot. normal contacts
    contacts_tra_shear = 0 # Total number of trans. shear contacts
    contacts_rot_shear = 0 # Total number of rot. shear contacts
    contacts_tra_roll  = 0 # Total number of trans. rolling contacts
    contacts_rot_roll  = 0 # Total number of rot. rolling contacts
    contacts_total_energy = 0 # Total number of rot. rolling contacts

    intervals = 2000

    density_tra_norm  = np.zeros((intervals,), dtype=int)
    density_rot_norm  = np.zeros((intervals,), dtype=int)
    density_tra_shear = np.zeros((intervals,), dtype=int)
    density_rot_shear = np.zeros((intervals,), dtype=int)
    density_tra_roll  = np.zeros((intervals,), dtype=int)
    density_rot_roll  = np.zeros((intervals,), dtype=int)
    density_total_energy = np.zeros((intervals,), dtype=int)

    # traverse through several files in a folder
    current_array  = iii
    current_length = len(current_array)
    os.chdir(files_path) # Change the directory to where the files are
    for ii in range(0,current_length):
        for lines in fileinput.input([current_array[ii]]):
            str_values = lines.split(" ")
            tra_norm  = float(str_values[0])
            rot_norm  = float(str_values[1])
            tra_shear = float(str_values[2])
            rot_shear = float(str_values[3])
            tra_roll  = float(str_values[4])
            rot_roll  = float(str_values[5])

            total_energy = tra_norm + rot_norm + tra_shear + rot_shear + tra_roll + rot_roll

            # convert the current energy into logarithmic scale to put in the bins 
            # Check if the value is zero [it doesn't necessarily go to one for the mill operating speeds]
            
            # trans. norm binning
            if (tra_norm > 0.0) and (tra_norm < 1.0):
                tra_norm_i = round(-100.0 * math.log10(tra_norm))
                if (tra_norm_i < intervals): # ignoring contacts with energies less than 10^⁻²⁰
                    contacts_tra_norm = contacts_tra_norm + 1
                    density_tra_norm[tra_norm_i] = density_tra_norm[tra_norm_i] + 1
                else:
                    faulty_contacts = faulty_contacts + 1
            else:
                faulty_contacts = faulty_contacts + 1

            # rot. norm binning
            if (rot_norm > 0.0) and (rot_norm < 1.0):
                rot_norm_i = round(-100.0 * math.log10(rot_norm))
                if (rot_norm_i < intervals): # ignoring contacts with energies less than 10^⁻²⁰
                    contacts_rot_norm = contacts_rot_norm + 1
                    density_rot_norm[rot_norm_i] = density_rot_norm[rot_norm_i] + 1
                else:
                    faulty_contacts = faulty_contacts + 1
            else:
                faulty_contacts = faulty_contacts + 1
            
            # tra. shear binning
            if (tra_shear > 0.0) and (tra_shear < 1.0):
                tra_shear_i = round(-100.0 * math.log10(tra_shear))
                if (tra_shear_i < intervals): # ignoring contacts with energies less than 10^⁻²⁰
                    contacts_tra_shear = contacts_tra_shear + 1
                    density_tra_shear[tra_shear_i] = density_tra_shear[tra_shear_i] + 1
                else:
                    faulty_contacts = faulty_contacts + 1
            else:
                faulty_contacts = faulty_contacts + 1

            # rot. shear binning
            if (rot_shear > 0.0) and (rot_shear < 1.0):
                rot_shear_i = round(-100.0 * math.log10(rot_shear))
                if (rot_shear_i < intervals): # ignoring contacts with energies less than 10^⁻²⁰
                    contacts_rot_shear = contacts_rot_shear + 1
                    density_rot_shear[rot_shear_i] = density_rot_shear[rot_shear_i] + 1
                else:
                    faulty_contacts = faulty_contacts + 1
            else:
                faulty_contacts = faulty_contacts + 1
            
            # tra. roll binning
            if (tra_roll > 0.0) and (tra_roll < 1.0):
                tra_roll_i = round(-100.0 * math.log10(tra_roll))
                if (tra_roll_i < intervals): # ignoring contacts with energies less than 10^⁻²⁰
                    contacts_tra_roll = contacts_tra_roll + 1
                    density_tra_roll[tra_roll_i] = density_tra_roll[tra_roll_i] + 1
                else:
                    faulty_contacts = faulty_contacts + 1
            else:
                faulty_contacts = faulty_contacts + 1

            # rot. roll binning
            if (rot_roll > 0.0) and (rot_roll < 1.0):
                rot_roll_i = round(-100.0 * math.log10(rot_roll))
                if (rot_roll_i < intervals): # ignoring contacts with energies less than 10^⁻²⁰
                    contacts_rot_roll = contacts_rot_roll + 1
                    density_rot_roll[rot_roll_i] = density_rot_roll[rot_roll_i] + 1
                else:
                    faulty_contacts = faulty_contacts + 1
            else:
                faulty_contacts = faulty_contacts + 1

            # total energy binning
            if (total_energy > 0.0) and (total_energy < 1.0):
                total_energy_i = round(-100.0 * math.log10(total_energy))
                if (total_energy_i < intervals): # ignoring contacts with energies less than 10^⁻²⁰
                    contacts_total_energy = contacts_total_energy + 1
                    density_total_energy[total_energy_i] = density_total_energy[total_energy_i] + 1
                else:
                    faulty_contacts_unique = faulty_contacts_unique + 1
            else:
                faulty_contacts_unique = faulty_contacts_unique + 1

            #break

    #print("Number of lines: ",count)

    # Cumulative Sum Calculation
    '''
    cumulative_tra_norm  = density_tra_norm.cumsum()
    cumulative_rot_norm  = density_rot_norm.cumsum()
    cumulative_tra_shear = density_tra_shear.cumsum()
    cumulative_rot_shear = density_rot_shear.cumsum()
    cumulative_tra_roll  = density_tra_roll.cumsum()
    cumulative_rot_roll  = density_rot_roll.cumsum()
    cumulative_total_energy  = density_total_energy.cumsum()
    '''
    # Reverse the cumulative sum as the lowest energies are sitting at the last points
    cumulative_tra_norm  = np.cumsum(density_tra_norm[::-1])
    cumulative_rot_norm  = np.cumsum(density_rot_norm[::-1])
    cumulative_tra_shear = np.cumsum(density_tra_shear[::-1])
    cumulative_rot_shear = np.cumsum(density_rot_shear[::-1])
    cumulative_tra_roll  = np.cumsum(density_tra_roll[::-1])
    cumulative_rot_roll  = np.cumsum(density_rot_roll[::-1])
    cumulative_total_energy  = np.cumsum(density_total_energy[::-1])

    # Normalize with respective contacts
    cumulative_tra_norm  = np.cumsum(density_tra_norm[::-1])/contacts_tra_norm
    cumulative_rot_norm  = np.cumsum(density_rot_norm[::-1])/contacts_rot_norm
    cumulative_tra_shear = np.cumsum(density_tra_shear[::-1])/contacts_tra_shear
    cumulative_rot_shear = np.cumsum(density_rot_shear[::-1])/contacts_rot_shear
    cumulative_tra_roll  = np.cumsum(density_tra_roll[::-1])/contacts_tra_roll
    cumulative_rot_roll  = np.cumsum(density_rot_roll[::-1])/contacts_rot_roll
    cumulative_total_energy  = np.cumsum(density_total_energy[::-1])/contacts_total_energy

    
    # Plotting the distributions
    x_values_den = np.arange(0,len(density_total_energy),1)
    x_values_cum = np.arange(0,len(cumulative_total_energy),1)

    x_axis_density = np.power(10,x_values_den/-100)
    x_axis_cumulative = np.power(10,x_values_cum/-100)

    # Mean, Median, Standard Deviation, Variance

    # (Mean)
    mean_tra_norm  = sum(np.array(density_tra_norm)*np.array(x_axis_density))/contacts_tra_norm
    mean_rot_norm  = sum(np.array(density_rot_norm)*np.array(x_axis_density))/contacts_rot_norm
    mean_tra_shear = sum(np.array(density_tra_shear)*np.array(x_axis_density))/contacts_tra_shear
    mean_rot_shear = sum(np.array(density_rot_shear)*np.array(x_axis_density))/contacts_rot_shear
    mean_tra_roll  = sum(np.array(density_tra_roll)*np.array(x_axis_density))/contacts_tra_roll
    mean_rot_roll  = sum(np.array(density_rot_roll)*np.array(x_axis_density))/contacts_rot_roll
    mean_total_energy = sum(np.array(density_total_energy)*np.array(x_axis_density))/contacts_total_energy

    # (Median)
    index = np.where(density_tra_norm == max(density_tra_norm)) # index is a tuple i.e., a nd-array (here 2-D)
    median_tra_norm  = x_axis_density[index[0][0]]

    index = np.where(density_rot_norm == max(density_rot_norm))
    median_rot_norm  = x_axis_density[index[0][0]]

    index = np.where(density_tra_shear == max(density_tra_shear))
    median_tra_shear = x_axis_density[index[0][0]]

    index = np.where(density_rot_shear == max(density_rot_shear))
    median_rot_shear = x_axis_density[index[0][0]]

    index = np.where(density_tra_roll == max(density_tra_roll))
    median_tra_roll  = x_axis_density[index[0][0]]

    index = np.where(density_rot_roll == max(density_rot_roll))
    median_rot_roll  = x_axis_density[index[0][0]]

    index = np.where(density_total_energy == max(density_total_energy))
    median_total_energy = x_axis_density[index[0][0]]

    # (Standard Deviation)
    diff_square  = (np.array(x_axis_density)-mean_tra_norm)*(np.array(x_axis_density)-mean_tra_norm)
    multiply_rep = diff_square * np.array(density_tra_norm)
    std_tra_norm = math.sqrt(sum(multiply_rep)/contacts_tra_norm)

    diff_square  = (np.array(x_axis_density)-mean_rot_norm)*(np.array(x_axis_density)-mean_rot_norm)
    multiply_rep = diff_square * np.array(density_rot_norm)
    std_rot_norm = math.sqrt(sum(multiply_rep)/contacts_rot_norm)

    diff_square  = (np.array(x_axis_density)-mean_tra_shear)*(np.array(x_axis_density)-mean_tra_shear)
    multiply_rep = diff_square * np.array(density_tra_shear)
    std_tra_shear = math.sqrt(sum(multiply_rep)/contacts_tra_shear)

    diff_square  = (np.array(x_axis_density)-mean_rot_shear)*(np.array(x_axis_density)-mean_rot_shear)
    multiply_rep = diff_square * np.array(density_rot_shear)
    std_rot_shear = math.sqrt(sum(multiply_rep)/contacts_rot_shear)

    diff_square  = (np.array(x_axis_density)-mean_tra_roll)*(np.array(x_axis_density)-mean_tra_roll)
    multiply_rep = diff_square * np.array(density_tra_roll)
    std_tra_roll = math.sqrt(sum(multiply_rep)/contacts_tra_roll)

    diff_square  = (np.array(x_axis_density)-mean_rot_roll)*(np.array(x_axis_density)-mean_rot_roll)
    multiply_rep = diff_square * np.array(density_rot_roll)
    std_rot_roll = math.sqrt(sum(multiply_rep)/contacts_rot_roll)

    diff_square  = (np.array(x_axis_density)-mean_total_energy)*(np.array(x_axis_density)-mean_total_energy)
    multiply_rep = diff_square * np.array(density_total_energy)
    std_total_energy = math.sqrt(sum(multiply_rep)/contacts_total_energy)
    
    # (Variance)
    variance_tra_norm  = std_tra_norm * std_tra_norm
    variance_rot_norm  = std_rot_norm * std_rot_norm
    variance_tra_shear = std_tra_shear * std_tra_shear
    variance_rot_shear = std_rot_shear * std_rot_shear
    variance_tra_roll  = std_tra_roll * std_tra_roll
    variance_rot_roll  = std_rot_roll * std_rot_roll
    variance_total_energy = std_total_energy * std_total_energy


    # Densities
    plt.semilogx(x_axis_density, density_tra_norm,  color="red",    label="density_tra_norm")
    plt.semilogx(x_axis_density, density_rot_norm,  color="green",  label="density_rot_norm")
    plt.semilogx(x_axis_density, density_tra_shear, color="blue",   label="density_tra_shear")
    plt.semilogx(x_axis_density, density_rot_shear, color="black",  label="density_rot_shear")
    plt.semilogx(x_axis_density, density_tra_roll,  color="yellow", label="density_tra_roll")
    plt.semilogx(x_axis_density, density_rot_roll,  color="magenta",label="density_rot_roll")

    plt.semilogx(x_axis_density, density_total_energy,  color="peru",label="density_total_energy")

    plt.legend()
    os.chdir(save_path)
    plt.savefig(types[k]+'_density')
    #plt.show()
    plt.close()

    # cumulative
    plt.semilogx(x_axis_cumulative[::-1], cumulative_tra_norm,  color="red",    label="cumulative_tra_norm")
    plt.semilogx(x_axis_cumulative[::-1], cumulative_rot_norm,  color="green",  label="cumulative_rot_norm")
    plt.semilogx(x_axis_cumulative[::-1], cumulative_tra_shear, color="blue",   label="cumulative_tra_shear")
    plt.semilogx(x_axis_cumulative[::-1], cumulative_rot_shear, color="black",  label="cumulative_rot_shear")
    plt.semilogx(x_axis_cumulative[::-1], cumulative_tra_roll,  color="yellow", label="cumulative_tra_roll")
    plt.semilogx(x_axis_cumulative[::-1], cumulative_rot_roll,  color="magenta",label="cumulative_rot_roll")

    plt.semilogx(x_axis_cumulative[::-1], cumulative_total_energy,  color="peru",label="cumulative_total_energy")

    plt.legend()
    plt.savefig(types[k]+'_cumulative')
    #plt.xlim([np.power(10,-20),np.power(10,-2)])
    #plt.show()
    plt.close()

    # Write the data to different text files
    stats = types[k]+'_statistics.txt'
    if os.path.exists(stats):
        os.remove(stats)
    
    with open(stats,'w') as f:
        f.write('Number of Total Contacts: '+str(contacts_total_energy)+'\n')
        f.write('Number of Trans. Norm. Contacts: '+str(contacts_tra_norm)+'\n')
        f.write('Number of Rot. Norm. Contacts: '+str(contacts_rot_norm)+'\n')
        f.write('Number of Trans. Shear. Contacts: '+str(contacts_tra_shear)+'\n')
        f.write('Number of Rot. Shear. Contacts: '+str(contacts_rot_shear)+'\n')
        f.write('Number of Trans. Roll. Contacts: '+str(contacts_tra_roll)+'\n')
        f.write('Number of Rot. Roll. Contacts: '+str(contacts_rot_roll)+'\n')

        f.write('\n')

        f.write('Mean Value of Total Energies: '+str(mean_total_energy)+'\n')
        f.write('Mean Value of Trans. Norm. Energies: '+str(mean_tra_norm)+'\n')
        f.write('Mean Value of Rot. Norm. Energies: '+str(mean_rot_norm)+'\n')
        f.write('Mean Value of Trans. Shear. Energies: '+str(mean_tra_shear)+'\n')
        f.write('Mean Value of Rot. Shear. Energies: '+str(mean_rot_shear)+'\n')
        f.write('Mean Value of Trans. Roll. Energies: '+str(mean_tra_roll)+'\n')
        f.write('Mean Value of Rot. Roll. Energies: '+str(mean_rot_roll)+'\n')

        f.write('\n')

        f.write('Median Value of Total Energies: '+str(median_total_energy)+'\n')
        f.write('Median Value of Trans. Norm. Energies: '+str(median_tra_norm)+'\n')
        f.write('Median Value of Rot. Norm. Energies: '+str(median_rot_norm)+'\n')
        f.write('Median Value of Trans. Shear. Energies: '+str(median_tra_shear)+'\n')
        f.write('Median Value of Rot. Shear. Energies: '+str(median_rot_shear)+'\n')
        f.write('Median Value of Trans. Roll. Energies: '+str(median_tra_roll)+'\n')
        f.write('Median Value of Rot. Roll. Energies: '+str(median_rot_roll)+'\n')

        f.write('\n')

        f.write('Standard Deviation of Total Energies: '+str(std_total_energy)+'\n')
        f.write('Standard Deviation of Trans. Norm. Energies: '+str(std_tra_norm)+'\n')
        f.write('Standard Deviation of Rot. Norm. Energies: '+str(std_rot_norm)+'\n')
        f.write('Standard Deviation of Trans. Shear. Energies: '+str(std_tra_shear)+'\n')
        f.write('Standard Deviation of Rot. Shear. Energies: '+str(std_rot_shear)+'\n')
        f.write('Standard Deviation of Trans. Roll. Energies: '+str(std_tra_roll)+'\n')
        f.write('Standard Deviation of Rot. Roll. Energies: '+str(std_rot_roll)+'\n')

        f.write('\n')

        f.write('Variance of Total Energies: '+str(variance_total_energy)+'\n')
        f.write('Variance of Trans. Norm. Energies: '+str(variance_tra_norm)+'\n')
        f.write('Variance of Rot. Norm. Energies: '+str(variance_rot_norm)+'\n')
        f.write('Variance of Trans. Shear. Energies: '+str(variance_tra_shear)+'\n')
        f.write('Variance of Rot. Shear. Energies: '+str(variance_rot_shear)+'\n')
        f.write('Variance of Trans. Roll. Energies: '+str(variance_tra_roll)+'\n')
        f.write('Variance of Rot. Roll. Energies: '+str(variance_rot_roll)+'\n')

    density_dist = types[k]+'_energies_density.txt'
    if os.path.exists(density_dist):
        os.remove(density_dist)

    with open(density_dist,'w') as f:
        f.write('Energy[J]'+','+'Total_Frequency[-]'+','+'Frequency_Trans_Norm[-]'+','+'Frequency_Rot_Norm[-]'+','+'Frequency_Trans_Shear[-]'+','+'Frequency_Rot_Shear[-]'+','+'Frequency_Trans_Roll[-]'+','+'Frequency_Rot_Roll[-]'+'\n')
        for jj in range(len(x_axis_density),0,-1):
            f.write(str(x_axis_density[jj-1])+','+str(density_total_energy[jj-1])+','+str(density_tra_norm[jj-1])+','+str(density_rot_norm[jj-1])+','+str(density_tra_shear[jj-1])+','+str(density_rot_shear[jj-1])+','+str(density_tra_roll[jj-1])+','+str(density_rot_roll[jj-1])+'\n')

    # Reverse the array to save 
    mod_cumulative_total_energy = cumulative_total_energy[::-1]
    mod_cumulative_tra_norm  = cumulative_tra_norm[::-1]
    mod_cumulative_rot_norm  = cumulative_rot_norm[::-1]
    mod_cumulative_tra_shear = cumulative_tra_shear[::-1]
    mod_cumulative_rot_shear = cumulative_rot_shear[::-1]
    mod_cumulative_tra_roll  = cumulative_tra_roll[::-1]
    mod_cumulative_rot_roll  = cumulative_rot_roll[::-1]

    cumulative_dist = types[k]+'_energies_cumulative.txt'
    if os.path.exists(cumulative_dist):
        os.remove(cumulative_dist)
    
    with open(cumulative_dist,'w') as f:
        f.write('Energy[J]'+','+'Total_Cumulative[%]'+','+'Cumulative_Trans_Norm[%]'+','+'Cumulative_Rot_Norm[%]'+','+'Cumulative_Trans_Shear[%]'+','+'Cumulative_Rot_Shear[%]'+','+'Cumulative_Trans_Roll[%]'+','+'Cumulative_Rot_Roll[%]'+'\n')
        for jj in range(len(x_axis_density),0,-1):
            f.write(str(x_axis_cumulative[jj-1])+','+str(mod_cumulative_total_energy[jj-1])+','+str(mod_cumulative_tra_norm[jj-1])+','+str(mod_cumulative_rot_norm[jj-1])+','+str(mod_cumulative_tra_shear[jj-1])+','+str(mod_cumulative_rot_shear[jj-1])+','+str(mod_cumulative_tra_roll[jj-1])+','+str(mod_cumulative_rot_roll[jj-1])+'\n')

    k = k + 1


end = time.time()


print("Execution time in seconds: ",(end - start))
