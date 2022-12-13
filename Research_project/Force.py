import Harmonic_oscillator as ho

class oscillator_force:
    
    def __init__(self, os: ho.oscillator, damping_coefficient: float):
        self.k_coefficient = os.k
        self.damping_coefficient = damping_coefficient
    
    def get_coefficients(self):
        return [self.k_coefficient, self.damping_coefficient]
