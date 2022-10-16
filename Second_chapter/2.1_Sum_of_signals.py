import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

N = 10000
fig, [signal, frequency] = plt.subplots(nrows = 2, ncols = 1)

x = np.linspace(0, 0.22, N)
f_x = np.zeros(N)
for i in range(1,4):
    f_x += (4-i)*np.cos(i*50*np.pi*2*x)
signal.plot(x, f_x, "r-")
signal.set_xlabel("Time")
signal.set_ylabel("Signal")

f_fft = fftpack.fft(f_x)
Amplitude = np.abs(f_fft)
Amplitude /= np.amax(Amplitude)
freqs = fftpack.fftfreq(N, d = 0.22/N)
frequency.plot(freqs, Amplitude, "b-")
frequency.set_xlabel("Frequency")
frequency.set_ylabel("Amplitude")

plt.show()
