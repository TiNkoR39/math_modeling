
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


t = np.arange(0,2,0.1)
def radio_func(n,t):
    dndt = 2*n
    return dndt
n_0 = 10
n = odeint(radio_func,n_0,t)
plt.plot(t,n,color='r')








