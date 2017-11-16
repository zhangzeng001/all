# import socket
#
# phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#
# phone.bind(('127.0.0.1',8080))
# phone.listen(5)
#
# while True:
#     conn,client_addr = phone.accept()
#     print('client_addr')
#
#     while True:
#         try:
#             data = conn.recv(1024)
#             print('')