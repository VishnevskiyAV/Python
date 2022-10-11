# Создание клиентской части
# Создайте клиента, который отправляет серверу из предыдущего упражнения число 5, затем ещё число 10 и затем команду «stop».
# Убедитесь, что всё работает правильно, то есть сервер после первой команды должен прислать «50», после второй – «100», а
    #  после команды «stop» должен быть остановлен (то есть программа из предыдущего упражнения должна остановиться).

import socket

SERVER_ADDRESS = ('localhost', 8080)

client = socket.socket()
client.connect(SERVER_ADDRESS)
client.send(bytes("5", encoding="UTF-8"))
data = client.recv(4096)
print(data.decode("UTF-8"))

client = socket.socket()
client.connect(SERVER_ADDRESS)
client.send(bytes("10", encoding="UTF-8"))
data = client.recv(4096)
print(data.decode("UTF-8"))

client = socket.socket()
client.connect(SERVER_ADDRESS)
client.send(bytes("stop", encoding="UTF-8"))
data = client.recv(4096)
print(data.decode("UTF-8"))
