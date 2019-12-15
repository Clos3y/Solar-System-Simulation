import numpy as np

class Particle:
    """
    This class defines a particle with given cartesian coordinates for position, velocity, and acceleration; a mass, and; a name.

    Input
    ------
    position: numpy array of three floats, representing x,y,z respectively (empty by default)\n
    velocity: numpy array of three floats, representing v_x, v_y, v_z respectively (empty by default)\n
    acceleration: numpy array of three floats, representing a_x, a_y, a_z respectively ([0,-10,0]m s^-2 by default)\n
    name: a string which names the particular particle you define (Ball by default) \n
    mass: a float which represents the mass of the particle (1.0kg by default) \n

    All inputs are SI, i.e., metres for position, m/s for velocity, m s^-2 for acceleration, and kg for mass
    """
    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,-10,0], dtype=float), Name='Ball', Mass=1.0):    
        self.position = np.array(Position,dtype=float) #m
        self.velocity = np.array(Velocity,dtype=float) #m/s
        self.acceleration = np.array(Acceleration,dtype=float) #m s^2
        self.Name = Name
        self.mass = float(Mass) #kg

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.mass,self.position,self.velocity,self.acceleration)
    
    G = 6.67430*10**(-11) #m^3 kg^-1 s^-2

    def euler(self,deltaT):
        """
        The Euler method for updating the position and velocity of a particle

        Input
        -----
        deltaT: the timestep in seconds
        """
        self.position = self.position + self.velocity*float(deltaT)
        self.velocity = self.velocity + self.acceleration*float(deltaT)

    def cromer(self,deltaT):
        """
        The Euler-Cromer method for updating the position and velocity of a particle

        Input
        -----
        deltaT: the timestep in seconds
        """
        self.velocity = self.velocity + self.acceleration*float(deltaT)
        self.position = self.position + self.velocity*float(deltaT)

    def verlet(self,deltaT):
        """
        The Verlet method for updating the position and velocity of a particle. 

        Input
        -----
        deltaT: the timestep in seconds
        """
        self.position = self.position + self.velocity*float(deltaT) + 0.5*self.acceleration*float(deltaT)*float(deltaT)

        self.velocity = self.velocity + (self.acceleration)*float(deltaT)

    def kineticEnergy(self):
        """
        Returns the kinetic energy of a body in Joules
        """
        return self.mass*np.dot(self.velocity,self.velocity)
    
    def momentum(self):
        """
        Returns the momentum of a body as a numpy array, with units kg.m/s
        """
        return self.velocity*self.mass