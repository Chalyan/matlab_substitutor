import Harmonic_oscillator as ho
from Force import oscillator_force
import numpy as np
from matplotlib import pyplot as plt

sample = ho.oscillator(100, 1, 5, -10)
os_f = oscillator_force(sample, 5)

interval = np.linspace(0,12,2400)
solution = os_f.find_solution(interval)
plt.plot(interval, solution, '-')
plt.show()
