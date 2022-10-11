# Создание серверной части
# Создайте сервер, который получает число, умножает его на 10 и отправляет обратно клиенту.
# При получении команды «stop», сервер должен быть остановлен (в примере из урока это можно сделать, завершив бесконечный цикл с помощью break).

import socket

SERVER_ADDRESS = ('', 8080)

server = socket.socket()
server.bind(SERVER_ADDRESS)
server.listen(1)
print("Ждём подключения клиента...")
while True:
    c, a = server.accept()
    data = c.recv(4096)
    print("Получили от клиента:", data)
    b = data.decode("UTF-8")
    if b == "stop":
        c.send(bytes("The programm is finished", encoding="UTF-8"))
        break
    data=bytes(str(int(data) *10), "UTF-8" )
    c.send(data)
    c.close()