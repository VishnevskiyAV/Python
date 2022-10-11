#  Модификаторы доступа
# Сделайте у класса из предыдущего упражнения закрытыми все его поля.
# Добавьте методы get и set для всех полей. Поскольку полей всего 4, то должно быть 4 метода get и 4 метода set.
# Убедитесь, что доступа к полям уже нет за пределами класса.
# Проверьте работу методов get и set.
# Сделайте закрытый метод printlog(), в котором с помощью функции print() выводите значение переданного параметра.
# В методах get и set вызывайте метод printlog с параметром: «Запрошено свойство NAME» (для методов get) 
    # или «Изменено свойство NAME» (для методов set). Вместо NAME должно быть подставлено имя соответствующего свойства.

class Rectangle:
    __x = 0
    __y = 0
    __w = 0
    __h = 0
    def __init__(self, x, y, w, h):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
# Методы get
    def getX(self):
        return self.__printlog('Запрошено свойство X: '+ '[' + str(self.__x) + ']')
    def getY(self):
        return self.__printlog('Запрошено свойство Y: '+ '[' + str(self.__y) + ']')
    def getW(self):
        return self.__printlog('Запрошено свойство W: '+ '[' + str(self.__w) + ']')
    def getH(self):
        return self.__printlog('Запрошено свойство H: '+ '[' + str(self.__h) + ']')
# Методы set
    def setX(self, x):
        self.__x = x
        self.__printlog('Изменено свойство X: '+ str(self.__x))
    def setY(self, y):
        self.__y = y
        self.__printlog('Изменено свойство Y: '+ str(self.__y))
    def setW(self, w):
        self.__w = w
        self.__printlog('Изменено свойство W: '+ str(self.__w))
    def setH(self, h):
        self.__h = h
        self.__printlog('Изменено свойство H: '+ str(self.__h))
# другие методы
    def __printlog(self, name):
        print(name)
    def __str__(self):
        return "Прямоугольник c координатами ("+ str(self.__x) + "," + str(self.__y) + ") шириной " + str(self.__w) + " и высотой " + str(self.__h)
    def square(self, r):
        return self.__w * self.__h
    def perimeter(self, r):
        return (self.__w * self.__h)**2

    

r = Rectangle(5, 3, 10, 4)
r.getX()
r.getY()
r.getW()
r.getH()
print ('___________________')
r.setX(6)
r.setY(4)
r.setW(8)
r.setH(5)

