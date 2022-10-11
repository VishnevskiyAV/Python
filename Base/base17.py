# Исключения
# Узнайте, какое исключение появляется при делении числа на 0.
# Попросите пользователя ввести 2 числа.
# Выведите результат деления.
# Перехватите исключение при делении на 0 и выведите пользователю в качестве результата слово «бесконечность».

try:
    a = 12/0
except ZeroDivisionError:
    print("Сan't devide by zero")

while True:
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    try:   
        dev = float(a)/float(b)
    except ZeroDivisionError:   
        print("Infinity")
    except ValueError:
        print("One or more entered characters is not a number, try again") 
    else:
        print("The result of devided = ", dev)
        exit(0)
 
        