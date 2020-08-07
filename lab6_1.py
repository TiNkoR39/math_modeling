import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def cicloida(n=3,r=2):
    if n<=0:
        print('дурачок?')
    else:
        n = np.linspace(0, 2*n*np.pi, 50)
        x = r*(n-np.sin(n))
        y = r*(1-np.cos(n))
        plt.plot(x,y,color='g', label='Cicloida')
        plt.axis('equal')
        plt.grid()
        plt.savefig('cicloida.png')
        plt.cla()
def astr(n=3,r=2):
    if n<=0:
        print('дурачок?')
    else:
        n = np.linspace(0, 2*n*np.pi, 50)
        x = r*np.cos(n)**3
        y = r*np.sin(n)**3
        plt.plot(x,y,color='g', label='Cicloida')
        plt.axis('equal')
        plt.grid()
        plt.savefig('astroida.png') 
        plt.cla()
        

cicloida(5.3)
astr()

