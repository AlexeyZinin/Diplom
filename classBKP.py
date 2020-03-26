import numpy
s = 1.0


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
        # print("регулятор положения создан")

    def processing(self):
        """Обработка сигнала задания и сигнала с ДПП,
        выдача напряжения U на электронный усилитель"""
        u = ((self. t2 * (s ** 2) + self.t1 * s + 1) * (self.t1 * s + 1))\
            /((self.mu * s + 1) ** 2 * self.tu * s)
        return u


regular = ControlDevise(uxz1=1.0, ux=1.0, t1=1.0, t2=1.0, tu=1.0, mu=1.0,)
u = regular.processing()
print(u)

# class ElectronBooster:
#     """"Электронный усилитель"""
#
#     def __init__(self, u, ky):
#         """Инициализируем атрибуты: сигнал с регулятора положения ПП"""
#         self.u = u
#         self.ky = ky
#         # print("электронный усилитель создан")
#
#     def boosting(self):
#         """Обработка сигнала с регулятора положения ПП и выдача усиленного сигнала ..."""
#         uy = self.u * self.ky
#         return uy
#
# electrboost = ElectronBooster(u, 10)
# uy = electrboost.boosting()
# print(uy)
