# Создание класса
# Создайте класс прямоугольника со следующими свойства: координаты левого верхнего угла, ширина и высота.
# Создайте экземпляр этого класса.
# Измените значения его свойств и выведите их.

class Rectangle:
    x = 0
    y = 0
    w = 0 
    h = 0

r1 = Rectangle()
r1.x = 5
r1.y = 3
r1.w = 12
r1.h = 6
print("координаты левого верхнего угла = ", r1.x, ",", r1.y, "ширина = ", r1.w, "высота = ", r1.h)