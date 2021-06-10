import socket
import sys
PORT = 9002
BUFFER_SIZE = 1024
def run_TCP ():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost',PORT))
    server.listen(1)
    client, addres = server.accept()
    print (addres)
    while not False:
        print(client.recv(BUFFER_SIZE).decode())
    server.close()
    client.close()
def run_UDP ():
    server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    server.bind(('localhost',PORT))
    while 1:
        data , addres = server.recvfrom(1024)
        print (addres)
        print(data.decode())
if __name__ == "__main__":
    if sys.argv[1] == '-T':
        run_TCP()
    elif sys.argv[1]=='-U':
        run_UDP()
    elif sys.argv[1] != '-T' or sys.argv[1] !='-U':
        print("python server.py -T -включить в режиме TCP \n"
               "python server.py -U - включить в режим UDP")

