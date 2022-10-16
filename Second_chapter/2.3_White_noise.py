import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

N = 10000
fig, [signal, frequency] = plt.subplots(nrows = 2, ncols = 1)

x = np.linspace(0, 0.22, N)
f_x = np.sin(100*np.pi*2*x) + 0.5*np.random.randn(N)
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
