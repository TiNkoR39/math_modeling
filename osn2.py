import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


t = np.arange(1,50,0.1)

def mayatnik(z,t):
    v , x = z
    dvdt = -k*(x-l)/m - 0.2* v -g

    dxdt = v
    return dvdt, dxdt

x0 = -0.08
v0 = 0.5
k = 1/8
g = 10
m = 0.5
z0 = v0,x0
l = m*g/k
sol = odeint(mayatnik,z0,t)


plt.plot(t,sol[:,1])
