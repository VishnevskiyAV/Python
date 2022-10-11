# Функции
# Создайте функцию, которая проверяет чётное число передано в параметре или нет. Она должна возвращать True или False.
# Создайте функцию, которая принимает список и возвращает максимальное значение из списка.
# Создайте функцию с переменным числом аргументов, внутри которой должно выводиться среднее арифметическое переданных чисел.
#Примечание: среднее арифметическое чисел равно сумме этих чисел поделённое на их количество.

def even(number):
    if number >= 0:
        return True
    if number < 0:
        return False

def getmax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max

def average(*number):
    s = 0
    for n in number:
        s += n
    return s/len(number)

print(even(-4))
print(even(1))
print(getmax([1, 2, 6, 8, -4, 12]))
print(average(6, 4, 12, 18, 9))
print(average(2, 4, 8, 3, 2))