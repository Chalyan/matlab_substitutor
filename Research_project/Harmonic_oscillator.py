import math

class oscillator:
    
    def __init__(self, k: float, m: float, x: float, v:float):
        self._m = m
        self._k = k
        self._initial_x = x
        self._initial_v = v
    
    def get_frequency(self):
        return math.sqrt(self._k/self._m)
    
    def get_initial_conditions(self):
        return [self._initial_x, self._initial_v]
