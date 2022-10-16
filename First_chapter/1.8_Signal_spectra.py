import numpy as np
from scipy.stats import hypsecant
from scipy import fftpack
import matplotlib.pyplot as plt

N = int(input("Please imput the number of points: "))

fig, [plot1, plot2] = plt.subplots(nrows = 2, ncols = 1)
a = np.linspace(0, 10, N)
sech_a = hypsecant.pdf(a)
plot1.plot(a, sech_a, "r-")
plot1.set_xlabel("X coordinate")
plot1.set_ylabel("Function values")

A = fftpack.fft(sech_a)
freqs = fftpack.fftfreq(len(a))
plot2.plot(freqs, np.abs(A), "g.")
plot2.set_xlabel("Frequency")
plot2.set_ylabel("Corresponding amplitude")

plt.show()
