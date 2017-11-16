import socket
import subprocess
import struct
import json

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #SOCK_STREAM代表TCP协议
phone.bind(('127.0.0.1',8080))
phone.listen(5)

while True:
    conn,client_addr=phone.accept() #(套接字链接,客户端的ip和port)
    print(client_addr)
    print('conn=====>>',conn)

    while True: #通信循环
        #收消息
        try:
            cmd=conn.recv(1024) # 1024最大的限制
            if not cmd:break #针对linux系统

            #执行，拿到执行结果
            obj = subprocess.Popen(cmd.decode('gbk'), shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

            stdout_res=obj.stdout.read()
            stderr_res=obj.stderr.read()

            # 制作报头
            header_dic = {
                'filename': 'a.txt',
                'total_size': len(stdout_res)+len(stderr_res),
                'md5': 'xxxxxxxxx'
            }
            head_json = json.dumps(header_dic)
            head_bytes = head_json.encode('utf-8')




            #先发报头长度
            conn.send(struct.pack('i',len(head_bytes)))

            #先发报头
            conn.send(head_bytes)

            #再发真是的数据
            # conn.send(stdout_res+stderr_res)
            conn.send(stdout_res)
            conn.send(stderr_res)
        except ConnectionResetError:
            break

    #挂电话
    conn.close()

#关机
phone.close()