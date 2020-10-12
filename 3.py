import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def ve(v, t):
    dvdt = a - y*v**2
    return(dvdt)

v0 = 0
a = 5
y=0.006
t = np.arange(1,40,1)

speed_of_parenek = odeint(ve,v0,t)
plt.axis('equal')
plt.plot(t,speed_of_parenek)
