The working folder contains code that runs as expected.

Working Code
------------
>>>>>>>>
	Particle.py: a file which defines the 'Particle' class, used for the simulation
	SolarSystem.py: the file containing the 'SolarSystem' class, used for performing the calculations in the simulation, along with plotting and data retrieval. 
	testSolarSystem.py: a test file containing all eight solar bodies for running the simulation
 
To run the code, open the folder in a Python compiler, input your data into testSolarSystem.py, uncomment any options that you want to include in SolarSystem.py. Then, run testSolarSystem.py in terminal.

FAQ
---
Q: My bodies are flying away!

A: You've probably entered the position and velocity as km/s or another non-base-SI unit. All parameters are in base-SI (namely, the metre, second, and kilogram). Alternatively, your time-step may be too large, so the bodies are jumping massive distances.

Q: The code crashes on my computer!

A: Please email s.close@lancaster.ac.uk ASAP with your error codes.
