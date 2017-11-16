import socket
import struct
import json

#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议

#发起电话链接
phone.connect(('127.0.0.1',8080))


while True:
    #发消息
    cmd=input('>>: ').strip()
    if not cmd:continue
    phone.send(cmd.encode('gbk'))

    #先收报头长度
    struct_res=phone.recv(4)
    header_size=struct.unpack('i',struct_res)[0]

    #再收报头
    head_bytes=phone.recv(header_size)
    head_json=head_bytes.decode('utf-8')
    head_dic=json.loads(head_json)
    print(head_dic)

    #最收消息
    cmd_res=b''
    recv_size=0
    total_size=head_dic['total_size']
    while recv_size < total_size:
        recv_data=phone.recv(1024)
        cmd_res+=recv_data
        recv_size+=len(recv_data)

    print(cmd_res.decode('gbk'))

#关机
phone.close()











