import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

r0 = (1600/np.pi)**0.5
t = np.arange(0,6,0.1)
E = 1374
k = 0.00000007175
def square(r,t) :
    drdt = (r**3*E*abs(np.sin(t*2/24*np.pi))*k)**0.5
    return drdt
r = odeint(square,r0,t)
s = (r**2)*np.pi
plt.plot(t,s)
print(s[-1])

