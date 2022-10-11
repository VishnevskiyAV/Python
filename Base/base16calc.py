# Модули 
# Создайте свой модуль и подключите его в основном файле.
# Напишите в модули 3 функции, каждая из которых принимает список. Первая функция – получение максимального значения,
# вторая – получение минимального значения, третья – получение суммы всех элементов.
print("Подключаемый модуль")

def getmax(arr):
    max = arr[0]
    for s in arr:
        if s > max:
            max = s
    return max

def getmin(arr):
    min = arr[0]
    for s in arr:
        if s < min:
            min = s
    return min

def getsum(arr):
    sum = 0
    for s in arr:
        sum += s
    return sum


    
