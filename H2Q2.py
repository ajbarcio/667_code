import numpy as np
import matplotlib.pyplot as plt

f = 2*np.pi
T = 1/(f/(2*np.pi))

t = np.linspace(0,2,1001)
print(np.linspace(1,5,5))

V = 0
g = 1
for n in np.linspace(1,5,5):
    if n==4:
        g = 0.75
    elif n==5:
        g = 0.25
    
    V = V+4/((2*n-1)*np.pi)*np.sin((2*n-1)*2*np.pi*t)*g

plt.figure()
plt.plot(t,V)
plt.show()