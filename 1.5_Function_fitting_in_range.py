from matplotlib import pyplot as plt
import numpy as np

a = int(input("Please enter left bound: "))
b = int(input("Please enter right bound: "))
x = np.linspace(a,b+1,50)
f_x = 6*np.sin(x)
linear_polynomial = np.poly1d(np.polyfit(x, f_x, 1))
quadratic_polynomial = np.poly1d(np.polyfit(x, f_x, 2))
qubic_polynomial = np.poly1d(np.polyfit(x, f_x, 3))
plt.plot(x, f_x)
plt.plot(x, linear_polynomial(x))
plt.plot(x, quadratic_polynomial(x))
plt.plot(x, qubic_polynomial(x))
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.legend(["Original functian", "Linear fit", "Quadratic fit", "Qubic fit"])
plt.show()
