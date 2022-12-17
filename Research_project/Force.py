import Harmonic_oscillator as ho
from scipy.integrate import odeint
import numpy as np

class oscillator_force:
    
    def __init__(self, os: ho.oscillator, dc: float):
        self._oscillator = os
        self._damping_coefficient = dc
    
    def find_solution(self, interval):
        
        def model(conditions, interval):
            theta1 = conditions[1]
            theta2 = -((self._damping_coefficient/self._oscillator._m)*conditions[1] +
                        self._oscillator.get_frequency()**2*conditions[0])
            return [theta1, theta2]

        solution = odeint(model, self._oscillator.get_initial_conditions(), interval)
        return solution[:,0]

