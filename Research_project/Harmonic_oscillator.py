import math

class oscillator:
    
    def __init__(self, k: float, m: float):
        self.m = m
        self.k = k
    
    def get_frequency(self):
        frequency = math.sqrt(self.k/self.m)
        return frequency
