import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

r0 = (1600/np.pi)**0.5/100
t = np.arange(6,30,0.1)
E = 1374
k = 0.00011
def square(r,t) :
    dsdt = r**3*E*np.sin((t-6)*2/24*np.pi)*k*np.pi  
    return dsdt
s = odeint(square,r0,t)
s = s*10000
plt.plot(t,s)
#print(s[-1])

