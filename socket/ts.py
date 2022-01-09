from socket import *

IP = '127.0.0.1'
PORT = 50000
BUFLEN = 512

listenSocket = socket(AF_INET, SOCK_STREAM)

listenSocket.bind((IP, PORT))


listenSocket.listen(5)
print(f'服务端启动成功，在{PORT}端口等待客户端连接...')

data_Socket, addr = listenSocket.accept()
print('接受一个客户端连接：', addr)

while True:
    recved = data_Socket.recv(BUFLEN)
    if not recved:
        break

    info = recved.decode()
    print(f'收到对方信息： {info}')

    data_Socket.send(f'服务端接收到了信息{info}'.encode())

data_Socket.close()
listenSocket.close()