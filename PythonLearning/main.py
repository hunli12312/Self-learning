import matplotlib.pyplot as plt
import numpy as np
x = []
y = []
x3 = []
y3 = []
p = 100
for x1 in range (0,20):
    y1 = (x1 * x1) / (3)
    x.append(x1)
    y.append(y1)
for x2 in range (0,20):
    y2 = 3 * x2
    x3.append(x2)
    y3.append(y2)
plt.plot(x,y,x3,y3)
plt.axvline(x=12)
plt.show()
