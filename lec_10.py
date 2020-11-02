import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

t = np.arange(0,10,0.01)

def sistema_uravneniy(z,t):
    theta, omega = z
    dtheta_dt = omega
    domega_dt = -b*omega - c*np.sin(theta)
    return dtheta_dt, domega_dt
theta0 = np.pi - 0.1
omega0 = 0
z0 = theta0, omega0
b =0.25
c = 5.0
sol = odeint(sistema_uravneniy,z0,t)
plt.plot(sol[:,1],sol[:,0])
#plt.show()
plt.plot(t,sol[:,0])
#plt.show()
plt.plot(t,sol[:,1])