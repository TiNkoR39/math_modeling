import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

x = np.arange(0,10,0.01)
def narkomania(z, x):
    y,omega = z
    dydx = omega
    domega_dx = np.sin(y)*omega - 3*x*y -5 
    return dydx, domega_dx
y0=0.01
omega0 = 0.05
z0=y0,omega0
sol = odeint(narkomania,z0,x)
plt.plot(sol[:,1],sol[:,0])
