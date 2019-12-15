import numpy as np
from Particle import Particle
import matplotlib.pyplot as plt
import matplotlib
import math
from copy import deepcopy
from mpl_toolkits import mplot3d
from matplotlib import style
import time

class SolarSystem:
    """
    A class to simulate an N-body system, using one of two methods.

    Input
    --------
    ListOfBodies: A list of Particle objects which you want to simulate (empty by default)\n
    Delta: The time-step in seconds (6-s by default)\n
    Time: The starting time coordinate, in case you did want to input a specific time (0-s by default)\n
    Iterations: How many times you want to simulation to run and recalculate (2000 by default; must be an integer)\n
    Method: Which method to use to calculate values: 1 being Euler, 2 being Euler-Cromer, 3 being RK4\n
    """
    def __init__(self,ListOfBodies = [],Delta = 6,Time = 0,Iterations = 2000,Method = 1):
        self.delta = float(Delta) #s
        self.time = float(Time) #s
        self.listOfBodies = ListOfBodies
        self.iterations = int(Iterations) #integer
        self.method = Method
        
    def __repr__(self):
        return 'Number of Bodies {0}, Time Coordinate: {1}s, Time-step: {2}s, Iterations: {3} --> Total Simulation Time: {4}s'.format(len(self.listOfBodies),self.time,self.delta,self.iterations,self.iterations*self.delta)
    
    def calculation(self):
        """
        Perfoms the calculation of the updates for positions, velocity, and acceleration. Optional code can be uncommented to calculate the time, and save data including kinetic energy, momentum, and potential energy
        """
        #Data = [] #Empty list for positional data
        #Time = [] #Empty list for time
        #KE = [] #Empty list for kinetic energy of the system
        #MOM = [] #Empty list for the momentum of the system
        #POT = [] #Empty list for the potential energy of the system
        #VIR = [] #Empty list for the Virial Theorm calculation

        #tempKE = 0 #Temporary variables
        #tempMOM = 0 #Temporary variables
        #tempPOT = 0 #Temporary variables

        bodiesX = {} #Empty dictionary to contain body positions for plotting
        bodiesY = {} #Empty dictionary to contain body positions for plotting
        bodiesZ = {} #Empty dictionary to contain body positions for plotting

        ax = plt.axes(projection="3d") #Sets the axes for plotting as 3D

        t0 = time.time() #When the code starts running

        for body in self.listOfBodies: # Creates a dictionary entry with an empty list for each position component, for each body
            bodiesX[body] = []
            bodiesY[body] = []
            bodiesZ[body] = []

            bodiesX[body].append(body.position[0])
            bodiesY[body].append(body.position[1])
            bodiesZ[body].append(body.position[2])

            #tempKE = tempKE + body.kineticEnergy()
            #tempMOM = tempMOM + body.momentum()

            #for secondaryBody in self.listOfBodies: # Handles potential energy
                #if secondaryBody != body:
                    #magnitudeOfDistance = float(((np.linalg.norm(body.position)**2) + (np.linalg.norm(secondaryBody.position)**2) - 2*np.dot(body.position,secondaryBody.position))**(1/2))

                    #tempPOT = tempPOT - Particle.G*body.mass*secondaryBody.mass/magnitudeOfDistance   

        #KE.append(tempKE) #Appends the system's intial kinetic energy to the list
        #MOM.append(np.linalg.norm(tempMOM)) #Appends the system's intial momentum to the list
        #POT.append(tempPOT) #Appends the system's intial potential energy to the list
        #VIR.append(2*tempKE + tempPOT) #Appends the system's Virial Theorem calculation to the list
        #Time.append(self.time) #Appends the system's intial time to the system

        for steps in range(self.iterations): # Begins the number of iterations
        
            #bounceKE = 0 # Dummy variable to recalculate the kinetic energy for each body
            #bounceMoment = np.array([0,0,0]) # Dummy variable to recalculate the momentum for each body
            #bouncePotent = 0 # Dummy variable to recalculate the potential energy for each body

            for mainBody in self.listOfBodies: # The body in question

                mainBody.acceleration = np.array([0,0,0]) # Resets the acceleration for the next body
                
                estPos = mainBody.position + mainBody.velocity*self.delta # Calcualtes the next position crudely for the Verlet method

                for secondaryBody in self.listOfBodies: # The second body

                    estSecPos = secondaryBody.position + secondaryBody.velocity*self.delta # Calcualtes the next position crudely for the Verlet method, for the second body
                    
                    if mainBody.Name != secondaryBody.Name: # Checking it doesn't act on itself
                        
                        if (self.method == 1) or (self.method == 2): # Euler, Euler-Cromer
                            
                            magnitudeOfDistance = float(((np.linalg.norm(mainBody.position)**2) + (np.linalg.norm(secondaryBody.position)**2) - 2*np.dot(mainBody.position,secondaryBody.position))**(1/2))

                            mainBody.acceleration = mainBody.acceleration + (Particle.G*secondaryBody.mass/(magnitudeOfDistance*magnitudeOfDistance*magnitudeOfDistance))*(secondaryBody.position - mainBody.position)
                     
                            #bouncePotent = bouncePotent - Particle.G*mainBody.mass*secondaryBody.mass/magnitudeOfDistance

                        elif self.method == 3: #Verlet. Holy hell, it works!

                            magnitudeOfCopy = float(((np.linalg.norm(estPos)**2) + (np.linalg.norm(estSecPos)**2) - 2*np.dot(estPos,estSecPos))**(1/2))

                            magnitudeOfDistance = float(((np.linalg.norm(mainBody.position)**2) + (np.linalg.norm(secondaryBody.position)**2) - 2*np.dot(mainBody.position,secondaryBody.position))**(1/2))
                            
                            estAcc = (Particle.G*secondaryBody.mass/(magnitudeOfCopy*magnitudeOfCopy*magnitudeOfCopy))*(estSecPos - estPos)
                            
                            acceleration =  (Particle.G*secondaryBody.mass/(magnitudeOfDistance*magnitudeOfDistance*magnitudeOfDistance))*(secondaryBody.position - mainBody.position)
                            
                            mainBody.acceleration = mainBody.acceleration + (estAcc+acceleration)*0.5

                            #bouncePotent = bouncePotent - Particle.G*mainBody.mass*secondaryBody.mass/magnitudeOfDistance                        
                        else:
                            raise ValueError('No such method exists!')

            self.time = self.time + self.delta # Updates time
            #Time.append(self.time) # Appends the new time to the time list

            for bodyUpdate in self.listOfBodies: # Updates positions, velocities and plots

                bodiesX[bodyUpdate].append(bodyUpdate.position[0])
                bodiesY[bodyUpdate].append(bodyUpdate.position[1])
                bodiesZ[bodyUpdate].append(bodyUpdate.position[2])

                #bounceKE = bounceKE + bodyUpdate.kineticEnergy()
                #bounceMoment = bounceMoment + bodyUpdate.momentum()

                if self.method == 1:
                    bodyUpdate.euler(self.delta)
                elif self.method == 2:
                    bodyUpdate.cromer(self.delta)
                elif self.method == 3:
                    bodyUpdate.verlet(self.delta)

            #MOM.append(np.linalg.norm(bounceMoment))
            #KE.append(bounceKE)
            #POT.append(bouncePotent)
            #VIR.append(2*bounceKE + bouncePotent)

        bigList = [] # Used to set the axes

        for body in self.listOfBodies:

            ax.plot3D(bodiesX[body],bodiesY[body],bodiesZ[body],':')
            ax.scatter3D(bodiesX[body][-1],bodiesY[body][-1],bodiesZ[body][-1],label=body.Name)

            bigList.append(max(np.absolute(bodiesX[body])))
            bigList.append(max(np.absolute(bodiesY[body])))
            bigList.append(max(np.absolute(bodiesZ[body])))
        
        BigValue = max(bigList)
        plt.legend()
        ax.set_xlim3d(-BigValue,BigValue)
        ax.set_ylim3d(-BigValue,BigValue)
        ax.set_zlim3d(-BigValue,BigValue)
        ax.set_xlabel('x/m')
        ax.set_ylabel('y/m')
        ax.set_zlabel('z/m')

        t1 = time.time()

        print('Computational time',t1-t0)
        print('Plotting...')
        plt.show()

        #np.save('POT_10s_Verlet',POT)
        #np.save('VIR_LongRun_Verlet',VIR)
        #np.save('KE_10s_Verlet',KE)
        #np.save('MOM_10s_Verlet',MOM)
        #np.save('LongRun',Time)