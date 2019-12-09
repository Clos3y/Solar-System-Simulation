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
        self.delta = float(Delta)
        self.time = float(Time)
        self.listOfBodies = ListOfBodies
        self.iterations = int(Iterations)
        self.method = Method
        
    def __repr__(self):
        return 'Number of Bodies {0}, Time Coordinate: {1}s, Time-step: {2}s, Iterations: {3} --> Total Simulation Time: {4}s'.format(len(self.listOfBodies),self.time,self.delta,self.iterations,self.iterations*self.delta)
    
    def calculation(self):

        Data = []
        Time = []
        KE = []
        MOM = []
        tempKE = 0
        tempMOM = 0

        # Data handling
        bodiesX = {}
        bodiesY = {}
        bodiesZ = {}

        Time = []

        fig = plt.figure()
        ax = plt.axes(projection="3d")

        for body in self.listOfBodies: # Creates a dictionary entry with an empty set for each position component
            bodiesX[body] = []
            bodiesY[body] = []
            bodiesZ[body] = []

            bodiesX[body].append(body.position[0])
            bodiesY[body].append(body.position[1])
            bodiesZ[body].append(body.position[2])

            tempKE = tempKE + body.kineticEnergy()
            tempMOM = tempMOM + np.linalg.norm(body.momentum())

        KE.append(tempKE)
        MOM.append(tempMOM)
        Time.append(self.time)

        for steps in range(self.iterations): #How many iterations
        
            bounceKE = 0
            bounceMoment = 0
            for mainBody in self.listOfBodies: # The body in question

                mainBody.acceleration = np.array([0,0,0]) # Resets the acceleration for the next body
                
                for secondaryBody in self.listOfBodies: # The bodies acting on it
                    
                    if mainBody.Name != secondaryBody.Name: # Checking it doesn't act on itself
                        
                        magnitudeOfDistance = 0
                        
                        if self.method == 1 or 2: # Euler, Euler-Cromer, Verlet
                            
                            magnitudeOfDistance = float(((np.linalg.norm(mainBody.position)**2) + (np.linalg.norm(secondaryBody.position)**2) - 2*np.dot(mainBody.position,secondaryBody.position))**(1/2))

                            mainBody.acceleration = mainBody.acceleration + (Particle.G*secondaryBody.mass/(magnitudeOfDistance*magnitudeOfDistance*magnitudeOfDistance))*(secondaryBody.position - mainBody.position)
                        
                        elif self.method == 3: #heun. work on this 
                            estVel = mainBody.velocity + mainBody.acceleration*self.delta

                            estPos = mainBody.position + estVel*self.delta

                            magnitudeOfCopy = float(((np.linalg.norm(estPos)**2) + (np.linalg.norm(secondaryBody.position)**2) - 2*np.dot(estPos,secondaryBody.position))**(1/2))

                            magnitudeOfDistance = float(((np.linalg.norm(mainBody.position)**2) + (np.linalg.norm(secondaryBody.position)**2) - 2*np.dot(mainBody.position,secondaryBody.position))**(1/2))
                            
                            estAcc = (Particle.G*secondaryBody.mass/(magnitudeOfCopy*magnitudeOfCopy*magnitudeOfCopy))*(secondaryBody.position - estPos)

                            acceleration =  (Particle.G*secondaryBody.mass/(magnitudeOfDistance*magnitudeOfDistance*magnitudeOfDistance))*(secondaryBody.position - mainBody.position)

                            mainBody.acceleration = mainBody.acceleration + (estAcc+acceleration)*0.5                        
                        else:
                            raise ValueError('No such method exists!')

            self.time = self.time + self.delta # Updates time
            Time.append(self.time)

            for bodyUpdate in self.listOfBodies: # Updates position and plots

                bodiesX[bodyUpdate].append(bodyUpdate.position[0])
                bodiesY[bodyUpdate].append(bodyUpdate.position[1])
                bodiesZ[bodyUpdate].append(bodyUpdate.position[2])

                bounceKE = bounceKE + bodyUpdate.kineticEnergy()
                bounceMoment = bounceMoment + np.linalg.norm(bodyUpdate.momentum())

                if self.method == 1:
                    bodyUpdate.euler(self.delta)
                elif self.method == 2:
                    bodyUpdate.cromer(self.delta)
                elif self.method == 3:
                    bodyUpdate.heun(self.delta)

            MOM.append(bounceMoment)
            KE.append(bounceKE)

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

        print('Plotting...')
        plt.show()

        np.save('Cromer_1000s_MOM',MOM)
        #np.save('1000s',Time)