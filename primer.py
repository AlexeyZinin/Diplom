# from control.matlab import *
# f = tf(1, [1, 1]);
# g = tf(1, [2 ,1]);
# w = f + g
# print(w)
# w = f* g
# print (w)
from control.matlab import *
import matplotlib.pyplot as plt

# """Пневматический цилиндр"""
# num1 = [1]
# den1 = [0.125, 0.2, 1]
# Wpc = tf(num1, den1)
# """ Найдем полюса и нули передаточной функции с использованием команд pole, zero"""
# print('Передаточная функция САУ : \n %s'%Wpc)
# print("Полюса: \n %s"%pole(Wpc))
# print("Нули:\n %s -\n "%zero(Wpc))
# y,x = step(Wpc)
# plt.plot(x,y,"b")
# plt.title('Step Responsse ')
# plt.ylabel('Amplitude')
# plt.xlabel('Time(sec)')
# plt.grid(True)
# plt.show()
# """Пневматический цилиндр Конец"""
#
"""Регулятор положения"""
num2 = [0.0375, 0.185, 0.5, 1]
den2 = [0.00000004, 0.00008, 0.04, 0]
wrp = tf(num2, den2)
""" Найдем полюса и нули передаточной функции с использованием команд pole, zero"""
print('Передаточная функция САУ : \n %s'%wrp)
print("Полюса: \n %s"%pole(wrp))
print("Нули:\n %s -\n "%zero(wrp))
y,x = step(wrp)
plt.plot(x,y,"b")
plt.title('Step Responsse ')
plt.ylabel('Amplitude')
plt.xlabel('Time(sec)')
plt.grid(True)
plt.show()
"""Регулятор положения Конец"""

"""Электропневматический преобразователь"""
num3 = [1.2]
den3 = [0.006, 0.3, 1]
wepp = tf(num3, den3)
""" Найдем полюса и нули передаточной функции с использованием команд pole, zero"""
print(f'Передаточная функция САУ : \n {wepp} \n')
print(f'Полюса: \n {pole(wepp)} \n')
print(f'Нули:\n {zero(wepp)} \n')
y,x = step(wepp)
plt.plot(x,y,"b")
plt.title('Step Responsse ')
plt.ylabel('Amplitude')
plt.xlabel('Time(sec)')
plt.grid(True)
plt.show()
"""Электропневматический преобразователь"""

