import socketserver
import json
import configparser
import os
from conf import settings


STATUS_CODE = {
    250:'aaaaa',
    252:'bbbbb',
    254:'=====>sucessful',
    257:'257'
}


class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            if not self.data:
                print('client closed...')
                break
            data = json.loads(self.data.decode())
            if data.get('action') is not None:
                print('---->',hasattr(self,'_auth'))
                if hasattr(self, "_%s" % data.get('action')):
                    func = getattr(self, "_%s" % data.get('action'))
                    func(data)
                else:
                    print('^^^^^^^^^^^')
                    self.send_response(250)
            else:
                print('^^^^^^^^^^^^^')
                self.send_response(250)

    def send_response(self ,status_code,data=None):
        #向客户端返回数据
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode())

    def _auth(self,*args,**kwargs):
        # print("-----auth",*args,**kwargs)
        data = args[0]
        if data.get("username") is None or data.get('password') is None:
            self.send_response(252)
        user = self.authenticate(data.get("username"), data.get("password"))
        if user is None:
            self.send_response(252)
        else:
            print("passed auth",user)
            self.user = user
            self.send_response(254)


    def authenticate(self,username,password):
        #验证用户合法性
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            if _password == password:
                print("pass auth..", username)
                config[username]["Username"] = username
                return config[username]

    def _put(self,*args,**kwargs):
        #客户端连接
        pass
    def _get(self,*args,**kwargs):
        data = args[0]
        if data.get('filename') is None:
            self.send_response(252)
        user_home_dir = "%s\\%s" % (settings.USER_HOME, self.user["Username"])
        file_abs_path = "%s\\%s" %(user_home_dir,data.get('filename'))
        print('file abs path',file_abs_path)
        if os.path.isfile(file_abs_path):
            print('----ready to send file')
            file_obj = open(file_abs_path,'rb')
            file_size = os.path.getsize(file_abs_path)
            self.send_response(257, data={'file_size':file_size})

            for i in file_obj:
                self.request.send(i)

            else:
                file_obj.close()
                print('send file done...')

        else:
            self.send_response(252)


    def _ls(self,*args,**kwargs):
        pass
    def _cd(self,*args,**kwargs):
        pass

if __name__ == '__main__':
    HOST, PORT = "127.0.0.1", 9999
