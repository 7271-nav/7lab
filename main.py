import socket
PORT = 9002
BUFFER_SIZE = 4096

def tcp():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(('localhost',PORT))
    while True:
        print('Input message')
        message =  input()
        client.send(message.encode())
def udp():
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    client.connect(('localhost',PORT))
    while True:
        print('Input message')
        message =  input()
        client.send(message.encode())
print('Введите -U, если UDP или -T, если TCP')
input_ = input()
if input_ == '-U':
    print('UDP start')
    udp()
elif input_ == '-T':
    print('TCP start')
    tcp()
