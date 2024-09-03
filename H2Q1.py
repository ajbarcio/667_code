import numpy as np
import matplotlib.pyplot as plt

f = 2*np.pi
T = 1/(f/(2*np.pi))

t = np.linspace(0,3*T,1001)

# Fundamental
V1 = 1/(np.pi)+np.sin(2*np.pi*t)/2
# First ten harmonics
V2 = V1
for i in np.linspace(2,10,5):
    V2 = V2-2/np.pi*(np.cos(2*i*np.pi*t)/((i-1)*(i+1)))

V3 = V1
for i in np.linspace(2,46,23):
    V3 = V3-2/np.pi*(np.cos(2*i*np.pi*t)/((i-1)*(i+1)))

plt.figure()
plt.plot(t,V1)
plt.figure()
plt.plot(t,V2)
plt.figure()
plt.plot(t,V3)
plt.show()