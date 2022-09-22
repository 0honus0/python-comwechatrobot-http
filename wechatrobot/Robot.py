from typing import Callable
import threading

import socketserver
import requests
import json

from .Api import Api
from .Bus import EventBus

Bus = EventBus()

class WeChatRobot:
    def __init__(self , ip : str = "0.0.0.0" , port : int = 23456):
        self.ip = ip
        self.port = port
        self.api = Api()
        #StartHook
        print(self.StartMsgHook(port = port))
        print(self.StartImageHook(save_path = ""))
        print(self.StartVoiceHook(save_path = ""))

        self.url = "http://{}:{}/".format(ip , port)

    def on(self , *event_type : str) -> Callable:
        def deco(func: Callable) -> Callable:
            for _type in event_type:
                Bus.subscribe( _type , func)
            return deco
        return deco

    def run(self , main_thread : bool = True):
        def receive_callback(data):
            return self.post(data)
        
        class ReceiveMsgSocketServer(socketserver.BaseRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

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

                        if 1 == msg["isSendMsg"]:
                            Bus.emit("self_msg", msg)
                        elif "chatroom" in msg["sender"]:
                            Bus.emit("group_msg", msg) 
                        else:
                            Bus.emit("friend_msg", msg)
                        
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
            print(e)
        return None

    # on_friend_msg = on("friend_msg")
    # on_group_msg  = on("group_msg")
    # on_self_msg =   on("self_msg")

    def __getattr__(self , item : str):
        return self.api.exec_command(item)

if __name__ == "__main__":
    robot = WeChatRobot()

    robot.run(main_thread = True)