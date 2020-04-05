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
    """Регулятор положения/натяжения ПП"""

    def __init__(self, uxz, ux1, ufz, un, t1, t2, tu, mu):
        """Инициализируем атрибуты: сигнал задания и сигнал с датчика поперечного положения / синал с датчика натяжения"""
        self.uxz = uxz
        self.ux1 = ux1
        self.ufz = ufz
        self.un = un
        self.t1 = t1
        self.t2 = t2
        self.tu = tu
        self.mu = mu
        # self.z = z
        # self.t = t
        # print("регулятор положения/натяжения создан")

    def processing1(self):
        """Обработка сигнала задания и сигнала с ДПП,
        выдача напряжения U на электронный усилитель"""
        Wrp = ((self.t2 * s ** 2 + self.t1 * s + 1) * (self.t1 * s + 1))\
             / (((self.mu * s + 1) ** 2) * self.tu * s)

        return Wrp

    def processing2(self):
        """Обработка сигнала задания и сигнала с ДН,
        выдача напряжения U на электронный усилитель"""
        Wrn = (self.t2 * s ** 2 + self.t1 * s + 1) / (self.tu * s)

        return Wrn

    def podstanovka1(self):
        """Подставнока оператора s в ПФ РП, для определения дискретной передаточной функции"""
        s = (z - 1) / z * t

        Wrpd = ((self.t2 * s ** 2 + self.t1 * s + 1) * (self.t1 * s + 1)) \
             / (((self.mu * s + 1) ** 2) * self.tu * s)

        return Wrpd

    def podstanovka2(self):
        """Подставнока оператора s в ПФ РН, для определения дискретной передаточной функции"""
        s = (z - 1) / z * t

        Wrnd = (self.t2 * s ** 2 + self.t1 * s + 1) / (self.tu * s)

        return Wrnd


class ElBooster:
    """Создаем класс электронный усилитель"""

    def __init__(self, u1, u2, ky):
        """Инициализируем атрибуты: сигнал с РП - u1, РН - u2"""
        self.u1 = u1
        self.u2 = u2
        self.ky = ky

    def boosting1(self):
        """Обработка сигнала с регулятора положения ПП и выдача усиленного сигнала ..."""
        uy1 = self.u1 * self.ky

        return uy1
    def boosting2(self):
        """Обработка сигнала с регулятора положения ПП и выдача усиленного сигнала ..."""
        uy2 = self.u2 * self.ky
        return uy2

class EPP:
    """Создадим класс электропневматический преобразователь"""

    def __init__(self, ):
        """Инициализируем атрибуты: """
# start = time.time

"Создание регулятор положения печатной пленки с необходимыми параметрами, выводим передаточную функцию регулятора"
regpol = ControlDevise(uxz=1, ux1=2, ufz=0, un=0, t1=0.2, t2=0.125, tu=0.04, mu=0.001)
Wrp = regpol.processing1()
Wrpd = regpol.podstanovka1()
print(f'Передаточная функция РП имеет вид \n Wрп(s) = {Wrp} \n')
print(f'Дискретная передаточная функция РП \n Wрп(s) = {Wrpd} \n')

"Создание регулятор натяжения печатной пленки с необходимыми параметрами, выводим передаточную функцию регулятора"
regnat = ControlDevise(uxz=0, ux1=0, ufz=1, un=1.2, t1=0.16, t2=0.06, tu=0.48, mu=0.001)
Wpn = regnat.processing2()
Wrnd = regnat.podstanovka2()
print(f'Передаточная функция РН имеет вид \n Wрн(s) = {Wpn} \n')
print(f'Дискретная передаточная функция РН \n Wрн(s) = {Wrnd} \n')

"Создание электронного усилителя 1"
elboost1 = ElBooster(u1=5, u2=0, ky=10)
uy1 = elboost1.boosting1()
print(f'Напряжение на выходе эл. усилителя 1 \n uy1 = {uy1} \n')

"Создание электронного усилителя 2"
elboost2 = ElBooster(u1=0, u2=4, ky=10)
uy2 = elboost2.boosting2()
print(f'Напряжение на выходе эл. усилителя 2 \n uy2 = {uy2} \n')






# ht = inverse_laplace_transform(fp, s, t)
#
# stop = time.time()
#
# f = lambdify(t, ht, 'numpy')
# tt = numpy.arange(0.01, 20, 0.05)
# plt.title('Переходные характеристики регуляторов \n с передаточными функциями: \n ПИД - W(s)=%s \n ПИ - W(s)=%s' % (fp, fpp))
# plt.plot(tt, f(tt), color='r', linewidth=2, label='ПИД-регулятор: h(t)=%s' % ht)
# plt.grid(True)
# plt.legend(loc='best')
# plt.show()



# regular1 = ControlDevise(uxz1=1, ux=2, t1=0.2, t2=0.125, tu=0.04, mu=0.001)
# fps = regular1.podstanovka()
# print(f'Дискретная передаточная функция имеет вид \n W(s) = {fps} \n')
#
# electrboost = ElBooster(fp, fps, 10)
# uy = electrboost.boosting()
# print(f'Сигнал с эл. усилителя \n Uy = {uy} \n')
