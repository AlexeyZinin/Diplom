# >>> print('Omega: \u03A9')
# Omega: Ω
# >>> print('Delta: \u0394')
# Delta: Δ
# >>> print('sigma: \u03C3')
# sigma: σ
# >>> print('mu: \u03BC')
# mu: μ
# >>> print('epsilon: \u03B5')
# epsilon: ε
# >>> print('degree: \u00B0')
# degree: °
# >>> print('6i\u0302 + 4j\u0302-2k\u0302')
# 6î + 4ĵ-2k
import time
import matplotlib.pyplot as plt
import numpy
from sympy import *
var('s, t, z')

class ControlDevise:
    """Регулятор положения ПП"""

    def __init__(self, uxz1, ux, t1, t2, tu, mu):
        """Инициализируем атрибуты: сигнал задания и сигнал с ДПП"""
        self.uxz1 = uxz1
        self.ux = ux
        self.t1 = t1
        self.t2 = t2
        self.tu = tu
        self.mu = mu
        # self.z = z
        # self.t = t
        # print("регулятор положения создан")

    def processing(self):
        """Обработка сигнала задания и сигнала с ДПП,
        выдача напряжения U на электронный усилитель"""
        fp = ((self.t2 * s ** 2 + self.t1 * s + 1) * (self.t1 * s + 1))\
             / (((self.mu * s + 1) ** 2) * self.tu * s)

        return fp
    def podstanovka(self):
        """одставнока оператора s в ПФ РП, для определения дискретной передаточной функции"""
        s = (z - 1) / z * t
        fp = ((self.t2 * s ** 2 + self.t1 * s + 1) * (self.t1 * s + 1)) \
             / (((self.mu * s + 1) ** 2) * self.tu * s)

        return fp

class ElBooster:
    """Создаем класс электронный усилитель"""

    def __init__(self, fp, fps, ky):
        """Инициализируем атрибуты: сигнал с регулятора ПП"""
        self.fp = fp
        self.fps = fps
        self.ky = ky

    def boosting(self):
        """Обработка сигнала с регулятора положения ПП и выдача усиленного сигнала ..."""
        uy = self.fps * self.ky

        return uy



start = time.time
regular = ControlDevise(uxz1=1, ux=2, t1=0.2, t2=0.125, tu=0.04, mu=0.001)
fp = regular.processing()
print(f'Передаточная функция имеет вид \n W(s) = {fp} \n')

ht = inverse_laplace_transform(fp, s, t)

stop = time.time()

f = lambdify(t, ht, 'numpy')
tt = numpy.arange(0.01, 20, 0.05)
plt.title('Переходные характеристики регуляторов \n с передаточными функциями: \n ПИД - W(s)=%s \n ПИ - W(s)=%s' % (fp, fpp))
plt.plot(tt, f(tt), color='r', linewidth=2, label='ПИД-регулятор: h(t)=%s' % ht)
plt.grid(True)
plt.legend(loc='best')
plt.show()



# regular1 = ControlDevise(uxz1=1, ux=2, t1=0.2, t2=0.125, tu=0.04, mu=0.001)
# fps = regular1.podstanovka()
# print(f'Дискретная передаточная функция имеет вид \n W(s) = {fps} \n')
#
# electrboost = ElBooster(fp, fps, 10)
# uy = electrboost.boosting()
# print(f'Сигнал с эл. усилителя \n Uy = {uy} \n')
