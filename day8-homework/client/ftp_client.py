import socket
import os,json
import optparse
import getpass


STATUS_CODE = {
    250:'aaaaa',
    252:'bbbbb',
    254:'======>sucessful'
}
class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="ftp server ip_addr")
        parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
        parser.add_option("-u", "--username", dest="username", help="username")
        parser.add_option("-p", "--password", dest="password", help="password")
        self.options , self.args = parser.parse_args()
        self.verify_args(self.options,self.args)
        self.make_connection()

    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.server,self.options.port))

    #校验parser参数
    def verify_args(self,options,args):
        if options.username is not None and options.password is not None:
            pass
        elif options.username is None and options.password is None:
            pass
        else:
            # if options.username is None or options.password is None:
            exit("输入用户名，密码")

        if options.server and options.port:
            # print(options)
            if options.port > 0 and options.port < 65535:
                return True
            else:
                print("-P  0-65535")

    #用户验证
    def authenticate(self):
        if self.options.username:
            print(self.options.username,self.options.password)
            return self.get_auth_result(self.options.username,self.options.password)
        else:
            retry_count = 0
            while retry_count <3:
                username = input("usename:").strip()
                password = input("password:").strip()
                return self.get_auth_result(username,password)


    def get_auth_result(self,user,password):
        data = {
            'action':'auth',
            'username':user,
            'password':password
        }
        self.sock.send(json.dumps(data).encode())
        response = self.get_response()
        if response.get('status_code') == 254:
            print('======>sucessful<=======')
            self.user = user
            return True
        else:
            print(response.get("status_msg"))

    #得到服务器端回复结果
    def get_response(self):
        data = self.sock.recv(1024)
        # print(data)
        data = json.loads(data.decode())
        return data
        # if data.get('status_code') == 254:
        #     print('======>sucessful<=======')
        #     return True
        # else:
        #     print(data.get("faled"))

    def interactive(self):
        if self.authenticate():
            print('start interactive iwth u')
            while True:
                choice = input("[%s]:"%self.user).strip()
                if len(choice) == 0:continue
                cmd_list = choice.split()
                print(hasattr(self,"_%s"%cmd_list[0]))
                if hasattr(self,"_%s"%cmd_list[0]):
                    func = getattr(self,"_%s"%cmd_list[0])
                    func(cmd_list)
                else:
                    print('XXXXXXXXXXXX')



    # def _get(self,cmd_list):
    #     print("get--",cmd_list)
    #     if len(cmd_list) == 1:
    #         print('文件名')
    #         return
    #     data_header = {
    #         'action': 'get',
    #         'filename': cmd_list[1]
    #     }
    #     self.sock.send(json.dumps(data_header).encode())
    #     response = self.get_response()
    #     print(response)
    def _get(self, cmd_list):
        print("get--", cmd_list)
        if len(cmd_list) == 1:
            print("no filename follows...")
            return
        data_header = {
            'action': 'get',
            'filename': cmd_list[1]
        }
        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()
        print(response)
        if response["status_code"] == 257:
            base_filename = cmd_list[1].split('\\')[-1]
            received_size = 0
            file_obj = open(base_filename,'wb')
            print(cmd_list[1])
            print("路径",base_filename)
            print('response',type(response['file_size']))
            while received_size < response['file_size']:
                data = self.sock.recv(1024)
                received_size += len(data)
                file_obj.write(data)
            else:
                print("传输完成")





if __name__ == '__main__':
    ftp = FTPClient()
    ftp.interactive()#交互