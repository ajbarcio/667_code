import numpy as np
import matplotlib.pyplot as plt

k = 32.4
m = 0.1
c = 10
amp   = 0.05

omega = 10

gain = 32.4/np.sqrt((k-m*omega**2)**2+(c*omega)**2)
# phase = -np.arctan(c*omega/(k-m*omega**2))
phase = -np.arctan2(c*omega,(k-m*omega**2))

print(gain)
print(phase)
print(amp*gain, "sin(", omega, "t +", phase, ")")

omega = 1000

gain = 32.4/np.sqrt((k-m*omega**2)**2+(c*omega)**2)
# phase = -np.arctan(c*omega/(k-m*omega**2))
phase = -np.arctan2(c*omega,(k-m*omega**2))

print(gain)
print(phase)
print(amp*gain, "sin(", omega, "t +", phase, ")")

omega = 10000

gain = 32.4/np.sqrt((k-m*omega**2)**2+(c*omega)**2)
# phase = -np.arctan(c*omega/(k-m*omega**2))
phase = -np.arctan2(c*omega,(k-m*omega**2))

print(gain)
print(phase)
print(amp*gain, "sin(", omega, "t +", phase, ")")