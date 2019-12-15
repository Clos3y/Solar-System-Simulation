from SolarSystem import SolarSystem
from Particle import Particle
import numpy as np

# The positional data used for this data starts on the 20th of Decemeber, 2017 at 00:00
# All data comes from Horizons JPL
# Position & velocity data has no uncertainty
# All positions are given in metres, velocities in metres per second, accelerations in metres per second per second, and mass in kilograms.

mercV = np.array([-5.051755059145317E+01, -2.488814855561766E+01, 2.600783790692931E+00])*1e3
mercP = np.array([-2.648428574136984E+07, 4.025512920600310E+07, 5.719026881601144E+06])*1e3
mercMass = 3.302e23

venuP = np.array([-2.517429237775515E+07, -1.056724463396861E+08,  3.174502116352320E+03])*1e3
venuV = np.array([3.382992741234366E+01, -8.259396312126476E+00, -2.065502269046253E+00])*1e3
venuMass = 4.8685e24

eartV = np.array([-3.026712722059201e1,  9.049458331142369e-1,  1.011930477240353e-3])*1e3
eartP = np.array([5.034383623318861e6,  1.471005883049705e8, -6.425463457882404e3])*1e3
eartMass = 5.972e24 

moonP = np.array([5.151034845980010e6,  1.467117832830890e8,  1.116060944650322e4])*1e3
moonV = np.array([-2.934096779216478e1,  1.187045472483821, -7.542971589742453e-2])*1e3
moonMass = 7.349e22

marsP = np.array([-2.426780015827827e8, -3.570019571553303e7,  5.207659249827221e6])*1e3
marsV = np.array([4.430961334311149, -2.190160191545871e1, -5.676920178302476e-1])*1e3
marsMass = 6.4171e23

jupiP = np.array([-6.456345388831882e8, -4.936787429592740e8,  1.649698529252595e7])*1e3
jupiV = np.array([7.785056290342203, -9.771285439115749, -1.336060195268289e-1])*1e3
jupiMass = 1898.13e24

satuP = np.array([-2.580001580880525e6, -1.505400238426360e9,  2.626833272809756e7])*1e3
satuV = np.array([9.138489314514731, -5.582877461640032e-2, -3.621731460402276e-1])*1e3
satuMass = 5.6834e26

uranP = np.array([2.654345091181264e9,  1.348937047690948e9, -2.935949538735342e7])*1e3
uranV = np.array([-3.126735892308242,  5.744067162096605,  6.201136228633741e-2])*1e3
uranMass = 86.813e24

neptP = np.array([4.288847528038050e9, -1.291632934435426e9, -7.224898808883280e7])*1e3
neptV = np.array([1.540804358197982,  5.228231198331880, -1.438864540842557e-1])*1e3
neptMass = 102.413e24

sunP = np.array([0,0,0])*1e3
sunV = np.array([0,0,0])*1e3
sunMass = 1988500e24

Neptune = Particle(neptP,neptV,np.array([0,0,0]),'Neptune',neptMass)
Uranus = Particle(uranP,uranV,np.array([0,0,0]),'Uranus',uranMass)
Saturn = Particle(satuP,satuV,np.array([0,0,0]),'Saturn',satuMass)
Jupiter = Particle(jupiP,jupiV,np.array([0,0,0]),'Jupiter',jupiMass)
Mars = Particle(marsP,marsV,np.array([0,0,0]),'Mars',marsMass)
Moon = Particle(moonP,moonV,np.array([0,0,0]),'Moon',moonMass)
Venus = Particle(venuP,venuV,np.array([0,0,0]),'Venus',venuMass)
Earth = Particle(eartP,eartV,np.array([0,0,0]),'Earth',eartMass)
Mercury = Particle(mercP,mercV,np.array([0,0,0]),'Mercury',mercMass)
Sun = Particle(np.array([0,0,0]),np.array([0,0,0]),np.array([0,0,0]),'Sun',sunMass)

# Ordered this way because the colours are nice
Planets = [Earth,Sun,Venus,Mars,Mercury,Jupiter,Moon,Saturn,Uranus,Neptune]
run = SolarSystem(Planets,12000,0,31536,3)
run.calculation()