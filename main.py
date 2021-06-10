import socket
PORT = 9002
BUFFER_SIZE = 4096

def tcp():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#создаем клиента для тсп
    client.connect(('localhost',PORT))#подключаемся к серверу
    while True:# цикл для взаимодействия
        print('Input message')#
        message =  input()#ввод с консоли
        client.send(message.encode())#отправляем серверу
def udp():#
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# создание клиента для юдп
    client.connect(('localhost',PORT))# соединение с сервером
    while True:#
        print('Input message')#
        message =  input()#
        client.send(message.encode())#отправляем серверу сообщение
print('Введите -U, если UDP или -T, если TCP')#
input_ = input()#ввод с консоли
if input_ == '-U':#если введено это то
    print('UDP start')#
    udp()#запускаем процедуру
elif input_ == '-T':#иначе если введено это, то
    print('TCP start')#
    tcp()# запускаем эту процедуру
