import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(1,20,0.1)

def xy(z,t):
    x, y = z
    dxdt = k1 * (a0 - x - y)
    dydt = k2 * (a0 - x - y)
    return dxdt, dydt

x0 = 0
y0 = 0
z0 = x0, y0
a0 = 10
k1 = 0.2
k2 = 0.1
sol = odeint(xy, z0, t)

plt.plot(t,sol[:,0])
plt.plot(t,sol[:,1])

