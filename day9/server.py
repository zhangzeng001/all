from socket import *


server = socket(AF_INET,SOCK_DGRAM)
server.bind(('127.0.0.1',8080))

while True:
    x = server.recvfrom(1024)
    msg,client_addr =




