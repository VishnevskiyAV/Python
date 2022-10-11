# Словари (ассоциативные массивы/map/hash map)
# Создайте словарь с двумя ключами «Name» и «Age» и значениями «Без имени» и «-1».
# Попросите пользователя ввести своё имя.
# Попросите пользователя ввести свой возраст.
# Примите эти данные и измените соответствующие элементы словаря.
# Выведите этот словарь (ключи и значения), используя цикл for.

mydict = dict(Name='No name', Age=-1,)
print(mydict)
name = input("Enter your name: ")
age = input("Enter your age: ")
mydict['Name'] = name
mydict['Age'] = age
for key in mydict:
    print(key, '=', mydict[key])

mydic = {str(i*2):i for i in range(1,5)}
print(mydic)