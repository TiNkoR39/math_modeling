import matplotlib.pyplot as plt 
import numpy as np


def kelvin_to_color(Kel=10000):
    ''' Функция возвращающая цвет (в RGB форме) цвезды, по температуре
        поверхности, подающейся на вход функции.
    '''
    Kel = Kel / 100
    # Вычисление красного
    if Kel <= 66:
        Red = 255
    else:
        Red = Kel - 60
        Red = 329.698727446*Red**(-0.1332047592)
        if Red < 0:
            Red = 0
        if Red > 255 :
            Red = 255
    r = Red / 255

    # Вычисление зелёного
    if Kel <= 66:
        Green = Kel
        Green = 99.4708025861 * np.log(Green) - 161.1195681661
        if Green < 0:
            Green = 0
        if Green > 255:
            Green = 255
    else:
        Green = Kel - 60
        Green = 288.1221695283 * Green**(-0.0755148492)
        if Green < 0:
            Green = 0
        if Green > 255:
            Green = 255
    g = Green / 255

    # Вычисление синего
    if Kel >= 66:
        Blue = 255
    else:
        if Kel <= 19:
            Blue = 0
        else:
            Blue = Kel - 10
            Blue = 138.5177312231 * np.log(Blue) - 305.0447927307
            if Blue < 0:
                Blue = 0
            if Blue > 255:
                Blue = 255
    b = Blue / 255
    x = [r,g,b]
    return x


rgb = []

bv = []
m = []
f = open('data_B_V.txt')
for i in f:
    bv.append(float(i))
f = open('data_B_V_1.txt')
for i in f:
    bv.append(float(i))
f = open('data_M.txt')
for i in f:
    m.append(float(i))
f = open('data_M_1.txt')
for i in f:
    m.append(float(i))
bv = np.array([bv])
m = np.array([m])

T = 4600*(1/(0.92* bv +1.7)+1/(0.92* bv +0.62))
for i in T[0]:
    rgb.append(kelvin_to_color(i))
plt.style.use(['dark_background'])
plt.plot(T[0],m[0],'.',markersize=0.05,c = rgb)
#plt.show()
