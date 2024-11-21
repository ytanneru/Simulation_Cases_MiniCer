# Simulation_Cases_MiniCer
Simulation cases described in the article, "Coupled CFD-DEM simulation of pin-type wet stirred media mills using immersed boundary approach and hydrodynamic lubrication force": https://doi.org/10.1016/j.powtec.2024.120060

**Pre-requisites:**
LIGGGHTS, OpenFOAM-6, cfdemCoupling, and their corresponding dependencies, Python (>3.6)
The versions of simulation softwares used in the simulation cases are taken from Institute for Particle Technology's (iPAT) GitLab repository: https://git.rz.tu-bs.de/partikeltechnik/

**Description:**
This repository provides the simulation cases to generate and run the simulation cases of the "stirred media mill" (MiniCeR). The simulations are setup to couple the CFD and DEM via two-way coupling and the corresponding files in the "Run" folder contain the post-processing scripts to extract the "collision/stress energies" and assemble them into a "collision/stress energy distribution". The simulations are setup in three stages, namely, "Init", "Stable", and "Run". The combinations of operating settings can be easily modified and the respective cases can be generated using the python scripts in the corresponding repositories. The scripts to run the simulations on the HPC-cluster systems are also added.
