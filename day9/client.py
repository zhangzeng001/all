from socket import *

client = socket(AF_INET,SOCK_DGRAM)



while True:
    msg = input(">>").strip()
    client.sendto(msg.encode('utf-8'),('127.0.0.1',8080))

