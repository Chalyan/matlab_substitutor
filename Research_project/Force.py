import Harmonic_oscillator as ho
from scipy.integrate import odeint
import numpy as np

class oscillator_force:
    
    def __init__(self, os: ho.oscillator, damping_coefficient: float):
        self.os = os
        self.damping_coefficient = damping_coefficient
    
    def find_solution(self, conditions, interval):
        
        def model(conditions, interval):
            theta1 = conditions[1]
            theta2 = -((self.damping_coefficient/self.os.m)*conditions[1] +
                        self.os.get_frequency()**2*conditions[0])
            return [theta1, theta2]

        solution = odeint(model, conditions, interval)
        return solution[:,0]

