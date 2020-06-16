import numpy as np
import matplotlib.pyplot as plt

plt.title("y=sin(x)")
plt.ylabel("sin(x)")
x=np.arange(4,10,0.01)
y=np.sin(x)
plt.grid()
plt.plot(x,y,'red')
plt.show()

