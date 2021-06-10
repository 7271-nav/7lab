# -*- coding: utf-8 -*-
import socket
import sys
PORT = 9002 #ставим порт
BUFFER_SIZE = 1024
# функция для работы с тсп
def run_TCP ():
    # создаем конфиги сервера
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #создаем адресс сервера
    server.bind(('localhost',PORT))
    server.listen(1)#слушаем порт по выбранному адресу
    client , addres = server.accept()# если клиент пришел то принимаем его
    print (addres)#пишем адрес клиента
    while not False:# бесконечный цикл для работы с клиентом
        print(client.recv(BUFFER_SIZE).decode())# получаем сообщение от клиента и выводим его
    server.close()#закрытие сервера
    client.close()#закрытие клиента
def run_UDP ():# процедура для работы с ЮДП
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# создаем сервер ЮДП
    server.bind(('localhost',PORT))# биндим адресс для сервера
    while 1 :# бесконечный цикл для работы сервера
        data , addres = server.recvfrom(1024)# получаем адрес и сообщение клиента
        print (addres)#печатаем адресс
        print(data.decode())#печатаем сообщение
if __name__ == "__main__":# для запуска из под командной строки
    if sys.argv[1] == '-T':#если параметр такой, то
        run_TCP()# запускаем эту процендуру
    elif sys.argv[1]=='-U':#иначе если параметр такой то
        run_UDP()# запускаем эту процедуру
    elif sys.argv[1] != '-T' or sys.argv[1] !='-U':# если ни один из этих параметров то выводим информацию
        print("python server.py -T -включить в режиме TCP \n"
               "python server.py -U - включить в режим UDP")

