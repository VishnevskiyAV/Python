# Conditional operator
print("Input two numbers: ")
num1 = input()
num2 = input()
if num2 != "0":
    rez = float(num1) / float(num2)
    print("Результат деления числа", num1,"на", num2, "=", rez)
elif num2 == "0":
    print("Infinity")
# Цикл While
# Напишите программу, которая будет принимать числа от пользователя и суммировать их, пока он не напишет слово «sum».
# Когда пользователь напишет слово «sum», должна быть выведена сумма всех чисел и начат процесс заново.
# Если пользователь напишет «exit» или «quit», программа должна быть завершена. 

print("________________________")
sum = 0
print("To sum all entered numbers, enter \"sum\"")
print("To exit enter \"exit\" or \"quit\"")
while True:
    x = input("Input any number: ")
    if x == "sum":
        print("The sum of all input numbers =", sum)
        sum = 0
        print("________________________")
        print("To sum all entered numbers, enter \"sum\"")
        print("To exit enter \"exit\" or \"quit\"")
        continue
    if x == "exit" or x == "quit":
        break
    sum += int(x)





