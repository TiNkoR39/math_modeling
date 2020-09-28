import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0,10**6,100)

def radio_func(m,t):
    dmdt = -k*m
    return dmdt
m_0 = 10
k_Ur_238 = 4.84*10**(-18)
k_Bi_210 = 1.61*10**(-6)
k_Ti_210 = 8.76*10**(-3)

k = k_Ur_238
m_ur_t = odeint(radio_func,m_0,t)
plt.plot(m_ur_t,t,color='r')
k = k_Bi_210
m_bi = odeint(radio_func,m_0,t)

plt.plot(m_bi,t,color='r')
k = k_Ti_210

m_ti = odeint(radio_func,m_0,t)
plt.plot(m_ti,t,color='r')





