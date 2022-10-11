# Абстрактные классы
# Сделайте класс автомобиля из предыдущего упражнения абстрактным.
# Сделайте метод движения у этого класса так же абстрактным.
# Создайте ещё один дочерний класс от класса автомобиля для ещё какой-нибудь конкретной модели и реализуйте абстрактный метод движения.
from abc import ABC, abstractmethod

class Auto(ABC):
    x = 0
    y = 0
    s = 0
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    @abstractmethod
    def mov(self):
        pass

class ferrari(Auto):
    m = 0
    def __init__(self, x, y, s, m):
        Auto.__init__(self, x, y, s)
        self.m = m
    def mov(self):
        print('Движение Ferrari в точку X: ' + str(self.x) + ' Y: ' + str(self.y)+ ' со скоростью: ' + str(self.s) + ' с ' + str(self.m) +' пассажирами')

class audi(Auto):
    m = 0
    def __init__(self, x, y, s, m):
        Auto.__init__(self, x, y, s)
        self.m = m
    def mov(self):
        print('Движение Audi в точку X: ' + str(self.x) + ' Y: ' + str(self.y)+ ' со скоростью: ' + str(self.s) + ' с ' + str(self.m) +' пассажирами')


a = audi(50, 30, 90, 4)
a.mov()
f = ferrari(10, 20, 120, 2)
f.mov()