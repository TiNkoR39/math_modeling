import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation 

c = 2.998e8
G = 6.672e-11
a = 20*149.6e9
m = 5*10**6*1.989e30
e = 0.8
r0 = a*(1+e)
phi0 = 0
T = ((4*np.pi/(G*m))**0.5)*a**(3/2)
t = np.arange(1,85*T,10)
l = (a*(1-e**2)*G*m)**0.5
rg = 2*G*m/(c**2)
v0 = 0
z0 = v0,r0,phi0
fr = len(t)


def shizika(z,t):
    
    vr, r, phi = z
    
    
    dvrdt = (-rg * c**2) / r**2 + (l**2)/(r**3) - (3 * (l**2) *rg)/r**4
    drdt = vr
    dphidt = 1/r**2
    
    return dvrdt, drdt, dphidt


sol = odeint(shizika,z0,t)
fig = plt.figure(figsize=(1,1))
ax = plt.subplot( polar=True)

Obj_1, = plt.plot([],[],'.',markersize = 8, color = 'y')
Obj_2,=plt.plot([],[],marker='o',markersize = 8, color='black')
def animate(i):
    Obj_1.set_data(sol[i,1],sol[i,2])
    Obj_2.set_data(0,0)
    
    
animation = animation.FuncAnimation(fig,animate,frames = fr, interval = 10)

animation.save('123.gif')
    
    
