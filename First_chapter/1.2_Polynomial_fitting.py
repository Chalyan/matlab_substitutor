import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 30, 3)
print("X points are: \n", x)
y = x**3
print("Y points are: \n", y)
plt.xlabel("X-values")
plt.ylabel("Y-values")
mymodel = np.poly1d(np.polyfit(x, y, 3))
# mymodel = np.poly1d(np.polyfit(x, y, 2)), to show imperfect fitting
myline = np.linspace(0, 27, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
