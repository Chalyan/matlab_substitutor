import Harmonic_oscillator as ho
from Force import oscillator_force
import numpy as np
from matplotlib import pyplot as plt

sample = ho.oscillator(100, 1)
print(sample.get_frequency())

os_f = oscillator_force(sample, 3)
print(os_f.os.get_frequency(), os_f.damping_coefficient)

interval = np.linspace(0,12,2400)
y0 = [5,0]
solution = os_f.find_solution(y0, interval)
plt.plot(interval, solution, '-')
plt.show()
