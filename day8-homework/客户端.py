import socket
import os
import json

client = socket.socket()
client.connect(('localhost',9000))

while True:
    #输入文件
    choice = input(">>").strip()
    if len(choice) == 0:continue
    #判断输入
    cmd_list = choice.split()
    # print(cmd_list[0])
    if cmd_list[0] == "put":
        if len(cmd_list) == 1:
            print('输入有误，"put filename"')
            continue
        filename = cmd_list[1]
        #判断文件是否存在
        if os.path.isfile(filename):
            file_obj = open(filename,'rb')
            #windows文件名
            base_filename = filename.split("\\")[-1]
            print(base_filename,os.path.getsize(filename))
            #动作、文件名、文件大小
            data_header = {
                "action":"put",
                "filename":base_filename,
                "size":os.path.getsize(filename)
            }
            client.send(json.dumps(data_header).encode())
            for i in file_obj:
                client.send(i)
            print("传输完成！")
        else:
            print("文件不存在")
    elif cmd_list[0] == "get":
        pass
    else:
        print('输入有误，"put filename"')