import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

h0=10000
h = np.arange(0,h0,100)

def xana_zemle(v,h):
    dvdr = 6.672e-11*5.972e24/(6.4e6+h0-h)**2/v
    return dvdr
v0=0.01
h1 = np.arange(h0,0,-100)
v = odeint(xana_zemle,v0,h)
#plt.axis('equal')
plt.plot(-h1,v)
print(v[-1])
