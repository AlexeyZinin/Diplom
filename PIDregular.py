from sympy import *
import time
import numpy

# РЕГУЛЯТОР ПОЛОЖЕНИЯ

# Объявляем символьную переменную
var('s')
# Объявляем переменные
uxz1 = 1
ux = 2
t1 = 0.2
t2 = 0.125
tu = 0.04
mu = 0.001
t = 1.2
z = 0.3
# Передаточная функция ПИДД2 регулятора с оператором s
fp = ((t2 * s ** 2 + t1 * s + 1) * (t1 * s + 1)) / ((mu * s + 1) ** 2) * tu * s
print(f'fp = {fp}')
s = (z - 1) / t * z
fp = ((t2 * s ** 2 + t1 * s + 1) * (t1 * s + 1)) / ((mu * s + 1) ** 2) * tu * s
print(f'fp = {fp}')
u = fp
print('u =', u)
# u = 25.0*(0.2*s + 1)*(0.125*s**2 + 0.2*s + 1)/(s*(0.001*s + 1)**2)

# ЭЛЕКТРОННЫЙ УСИЛИТЕЛЬ



