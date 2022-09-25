from typing import Callable
import threading
import logging
import socketserver
import requests
import json

from .Api import Api
from .Bus import EventBus

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

Bus = EventBus()

BASE_PATH = '''C:\\users\\user\My Documents\WeChat Files\\'''

class WeChatRobot:
    def __init__(self , ip : str = "0.0.0.0" , port : int = 23456):
        self.ip = ip
        self.port = port
        self.api = Api()

        self.url = "http://{}:{}/".format(ip , port)

    def on(self , *event_type : str) -> Callable:
        def deco(func: Callable) -> Callable:
            for _type in event_type:
                Bus.subscribe( _type , func)
            return deco
        return deco

    def run(self , main_thread : bool = True):
        #StartHook
        self.StartMsgHook(port = self.port)
        self.StartImageHook(save_path = "")
        self.StartVoiceHook(save_path = "")

        class ReceiveMsgSocketServer(socketserver.BaseRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def receive_callback(self , msg):
                if 1 == msg["isSendMsg"]:
                    Bus.emit("self_msg", msg)
                elif "chatroom" in msg["sender"]:
                    Bus.emit("group_msg", msg) 
                elif "gh" in msg["sender"]:
                    Bus.emit("public_msg", msg)
                else:
                    Bus.emit("friend_msg", msg)

            def handle(self):
                conn = self.request
                while True:
                    try:
                        ptr_data = b""
                        while True:
                            data = conn.recv(1024)
                            ptr_data += data
                            if len(data) == 0 or data[-1] == 0xA:
                                conn.sendall("200 OK".encode())
                                break
                        msg = json.loads(ptr_data.decode('utf-8'))
                        self.receive_callback(msg)
                    except OSError:
                        break
                    except json.JSONDecodeError:
                        pass
                conn.close()

        ip_port = ( self.ip , self.port )
        try:
            s = socketserver.ThreadingTCPServer(ip_port , ReceiveMsgSocketServer)
            if main_thread:
                s.serve_forever()
            else:
                socket_server = threading.Thread(target=s.serve_forever)
                socket_server.setDaemon(True)
                socket_server.start()
            return socket_server.ident
        except KeyboardInterrupt:
            pass
        except Exception as e:
            logging.error(e)
        return None

    def __getattr__(self , item : str):
        return self.api.exec_command(item)

if __name__ == "__main__":
    robot = WeChatRobot()

    robot.run(main_thread = True)