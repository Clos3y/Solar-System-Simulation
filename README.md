This is my Solar System simulation written in Python. It is poorly optimised and ugly, but so am I, so this code has a special place in my heart. Please don't submit any requests, because I probably will not change anything; what's done is done. I provide this as a basis for people to start building their own simulations from, or to take inspiration from.


Working Code
------------
Particle.py: a file which defines the 'Particle' class, used for the simulation
SolarSystem.py: the file containing the 'SolarSystem' class, used for performing the calculations in the simulation, along with plotting and data retrieval. 
testSolarSystem.py: a test file containing all eight solar bodies for running the simulation
 
To run the code, open the folder in a Python compiler, input your data into testSolarSystem.py, uncomment any options that you want to include in SolarSystem.py. Then, run testSolarSystem.py in terminal.

FAQ
---
Q: My bodies are flying away!

A: You've probably entered the position and velocity as km/s or another non-base-SI unit. All parameters are in base-SI (namely, the metre, second, and kilogram). Alternatively, your time-step may be too large, so the bodies are jumping massive distances.

Q: The code crashes on my computer!

A: If it's that bad, submit an issue and I might look at it.
