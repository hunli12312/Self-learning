from math import *
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import MultipleLocator
data = pd.read_excel(r'C:\Users\LiHao\Downloads\Car-following tutorial data.xlsx',engine='openpyxl')
X = data.iloc[1:34,1:2]
Y = data.iloc[37:157,0:2]
x_major_locator = MultipleLocator(10)
y_major_locator = MultipleLocator(30)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)
#plt.xlim(0,35)
#plt.ylim(350,420)
print (Y)
#plt.plot(X)
plt.plot(Y)
plt.show()