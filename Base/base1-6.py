# Вывод переменных
print("Hello")
print("Я прохожу курс по Python")
print("Я учу Python по курсу: ‘Программирование на Python с Нуля до Гуру’")
print()
print("Я прохожу курс по Python\nЯ учу Python по курсу: ‘Программирование на Python с Нуля до Гуру’")
print("____________________")
# Переменные и их типы
a = 10
print(a)
a = 15
print('значение переменной a =', a)
str = "Значение переменной"
str1 = "="
print(str,'a', str1, a)
true = True
false = False
print(str, 'true', str1,true)
print(str, 'false', str1, false)
# Maths expressions
print("____________________")
x = 10
y = 15
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x % y =", x % y)
print("x // y =", x // y)
print("x ** y =", x ** y)
print(((15 * 10 - 20) / 2) + 14 * 10 + (-45))
print("x =", x, "=", bin(x))
# Logical expressions
print("____________________")
x = True
y = False
print(x and (x or (y and x or y) and x or x != y))
print(15 > 20 or (5 < 7 and 8 > 12 or 12 >= 12 and 15 < 18))
# String expressions
print("____________________")
number1=input("Input first number: ")
number2=input("Input second number: ")
number3=input("Input third number: ")
print("Среднее арифмитическое чисел",number1, number2, number3, '=', (float(number1) + float(number2) + float(number3))/3)
