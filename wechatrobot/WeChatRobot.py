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

class WeChatRobot:
    BASE_PATH = "C:\\Users\\user\\My Documents\\WeChat Files"

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
        self.StartImageHook(save_path = self.BASE_PATH)
        self.StartVoiceHook(save_path = self.BASE_PATH)

        class ReceiveMsgSocketServer(socketserver.BaseRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def receive_callback(self , msg):
                type_dict = {
                    0      : 'eventnotify', # 成员变更 
                    1      : 'text',
                    3      : 'image',
                    9      : 'scancashmoney',            # 面对面付款
                    34     : 'voice',
                    35     : 'qqmail',
                    37     : 'friendrequest',
                    42     : 'card',
                    43     : 'video',
                    47     : 'animatedsticker',
                    48     : 'location',
                    49     : 'share',
                    50     : 'voip',
                    51     : 'phone',
                    106    : 'sysnotify',   # system notification 修改群名称
                    1009   : 'eventnotify', # 减少成员 
                    1010   : 'eventnotify', # 添加成员
                    2000   : 'transfer',
                    2001   : 'redpacket',
                    2002   : 'miniprogram',
                    2003   : 'groupinvite',
                    2004   : 'file',
                    2005   : 'revokemsg',
                    2006   : 'groupannouncement',
                    10000  : 'sysmsg',      # 拍一拍 语音消息 撤回消息 邀请入群 移出群
                    10002  : 'other'        # multivoip , taptap , ClientCheckConsistency, 邀请加入群聊并分享历史消息
                }

                msg['type'] = type_dict.get(msg['type'] , 'unhandled'+str(msg['type']))

                if msg["type"] == "friendrequest":
                    Bus.emit("frdver_msg" , msg)
                elif '<sysmsg type="revokemsg">' in msg["message"]:
                    Bus.emit("revoke_msg", msg)
                elif "微信转账" in msg["message"] and "<paysubtype>1</paysubtype>" in msg["message"]:
                    Bus.emit("transfer_msg", msg)
                elif (1 == msg["isSendMsg"]):
                    if 1 == msg["isSendByPhone"]:
                        Bus.emit("self_msg", msg)
                elif "chatroom" in msg["sender"]:
                    Bus.emit("group_msg", msg)
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
                    except UnicodeDecodeError as e:
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

    def get_base_path(self):
        return self.BASE_PATH

    def __getattr__(self , item : str):
        return self.api.exec_command(item)
