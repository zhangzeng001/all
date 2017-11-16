import optparse
from src.ftp_server import FTPHandler
import socketserver
from conf import settings

class ArgvHandler(object):
    def __init__(self):
        self.parser = optparse.OptionParser()
        (options,args) = self.parser.parse_args()

        self.verify_args(options, args)

    def verify_args(self,options,args):
        #检查并校验相应功能
        if hasattr(self,args[0]):
            func = getattr(self,args[0])
            func()
        else:
            self.parser.print_help()

    def start(self):
        print('启动server')

        server = socketserver.ThreadingTCPServer((settings.HOST,settings.PORT),FTPHandler)
        server.serve_forever()
        # self.parser = optparse.OptionParser()
        # (options, args) = self.parser.parse_args()
        # self.verify_args(options, args)




