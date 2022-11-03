from typing import Callable, Any, Union, Awaitable , Optional , Dict
import requests
import json
from .Modles import *
import base64
from wechatrobot import ChatRoomData_pb2 as ChatRoom

class Api:
    port : int = 18888
    db_handle : Dict[str, int] = 0

    def IsLoginIn(self , **params) -> Dict:
        return self.post(WECHAT_IS_LOGIN , IsLoginBody(**params))

    def GetSelfInfo(self , **params) -> Dict:
        return self.post(WECHAT_GET_SELF_INFO , GetSelfInfoBody(**params))

    def SendText(self , **params) -> Dict:
        return self.post(WECHAT_MSG_SEND_TEXT , SendTextBody(**params))

    def SendAt(self , **params) -> Dict:
        return self.post(WECHAT_MSG_SEND_AT , SendAtBody(**params))

    def SendCard(self , **params) -> Dict:
        return self.post(WECHAT_MSG_SEND_CARD , SendCardBody(**params))

    def SendImage(self , **params) -> Dict:
        return self.post(WECHAT_MSG_SEND_IMAGE , SendImageBody(**params))

    def SendFile(self , **params) -> Dict:
        return self.post(WECHAT_MSG_SEND_FILE , SendFileBody(**params))
    
    def SendArticle(self , **params) -> Dict:
        return self.post(WECHAT_MSG_SEND_ARTICLE , SendArticleBody(**params))

    def SendApp(self , **params) -> Dict:
        return self.post(WECHAT_MSG_SEND_APP , SendAppBody(**params))

    def StartMsgHook(self, **params) -> Dict:
        return self.post(WECHAT_MSG_START_HOOK , StartMsgHookBody(**params))

    def StopMsgHook(self , **params) -> Dict:
        return self.post(WECHAT_MSG_STOP_HOOK , StopMsgHookBody(**params))
    
    def StartImageHook(self , **params) -> Dict:
        return self.post(WECHAT_MSG_START_IMAGE_HOOK , StartImageHookBody(**params))

    def StopImageHook(self , **params) -> Dict:
        return self.post(WECHAT_MSG_STOP_IMAGE_HOOK , StopImageHookBody(**params))

    def StartVoiceHook(self , **params) -> Dict:
        return self.post(WECHAT_MSG_START_VOICE_HOOK  , StartVoiceHookBody(**params))

    def StopVoiceHook(self , **params) -> Dict:
        return self.post(WECHAT_MSG_STOP_VOICE_HOOK , StopVoiceHookBody(**params))

    def GetContactList(self , **params) -> Dict:
        return self.post(WECHAT_CONTACT_GET_LIST , GetContactListBody(**params))

    def CheckContactStatus(self , **params) -> Dict:
        return self.post(WECHAT_CONTACT_CHECK_STATUS , CheckContactStatusBody(**params))

    def DelContact(self , **params) -> Dict:
        return self.post(WECHAT_CONTACT_DEL , DelContactBody(**params))

    def SearchContactByCache(self , **params) -> Dict:
        return self.post(WECHAT_CONTACT_SEARCH_BY_CACHE , SearchContactByCacheBody(**params))

    def SearchContactByNet(self , **params) -> Dict:
        return self.post(WECHAT_CONTACT_SEARCH_BY_NET , SearchContactByNetBody(**params))

    def AddContactByWxid(self , **params) -> Dict:
        return self.post(WECHAT_CONTACT_ADD_BY_WXID , AddContactByWxidBody(**params))

    def AddContactByV3(self , **params) -> Dict:
        return self.post(WECHAT_CONTACT_ADD_BY_V3 , AddContactByV3Body(**params))

    def AddContactByPublicId(self , **params) -> Dict:
        return self.post(WECHAT_CONTACT_ADD_BY_PUBLIC_ID , AddContactByPublicIdBody(**params))

    def VerifyApply(self , **params) -> Dict:
        return self.post(WECHAT_CONTACT_VERIFY_APPLY , VerifyApplyBody(**params))

    def EditRemark(self , **params) -> Dict:
        return self.post(WECHAT_CONTACT_EDIT_REMARK , EditRemarkBody(**params))

    def GetChatroomMemberList(self , **params) -> Dict:
        return self.post(WECHAT_CHATROOM_GET_MEMBER_LIST , GetChatroomMemberListBody(**params))

    def GetChatroomMemberNickname(self , **params) -> Dict:
        return self.post(WECHAT_CHATROOM_GET_MEMBER_NICKNAME , GetChatroomMemberNicknameBody(**params))

    def DelChatroomMember(self , **params) -> Dict:
        return self.post(WECHAT_CHATROOM_DEL_MEMBER , DelChatroomMemberBody(**params))

    def AddChatroomMember(self , **params) -> Dict:
        return self.post(WECHAT_CHATROOM_ADD_MEMBER , AddChatroomMemberBody(**params))

    def SetChatroomAnnouncement(self , **params) -> Dict:
        return self.post(WECHAT_CHATROOM_SET_ANNOUNCEMENT , SetChatroomAnnouncementBody(**params))

    def SetChatroomName(self , **params) -> Dict:
        return self.post(WECHAT_CHATROOM_SET_CHATROOM_NAME , SetChatroomNameBody(**params))

    def SetChatroomSelfNickname(self , **params) -> Dict:
        return self.post(WECHAT_CHATROOM_SET_SELF_NICKNAME , SetChatroomSelfNicknameBody(**params))

    def GetDatabaseHandles(self , **params) -> Dict:
        return self.post(WECHAT_DATABASE_GET_HANDLES , GetDatabaseHandlesBody(**params))

    def BackupDatabase(self , **params) -> Dict:
        return self.post(WECHAT_DATABASE_BACKUP , BackupDatabaseBody(**params))

    def QueryDatabase(self , **params) -> Dict:
        return self.post(WECHAT_DATABASE_QUERY , QueryDatabaseBody(**params))

    def SetVersion(self , **params) -> Dict:
        return self.post(WECHAT_SET_VERSION , SetVersionBody(**params))

    def StartLogHook(self , **params) -> Dict:
        return self.post(WECHAT_LOG_START_HOOK , StartLogHookBody(**params))

    def StopLogHook(self , **params) -> Dict:
        return self.post(WECHAT_LOG_STOP_HOOK , StopLogHookBody(**params))

    def OpenBrowserWithUrl(self , **params) -> Dict:
        return self.post(WECHAT_BROWSER_OPEN_WITH_URL , OpenBrowserWithUrlBody(**params))

    def GetPublicMsg(self , **params) -> Dict:
        return self.post(WECHAT_GET_PUBLIC_MSG , GetPublicMsgBody(**params))

    def ForwardMessage(self , **params) -> Dict:
        return self.post(WECHAT_MSG_FORWARD_MESSAGE , ForwardMessageBody(**params))

    def GetQrcodeImage(self , **params):
        r = requests.post( f"http://127.0.0.1:{self.port}/api/?type={WECHAT_GET_QRCODE_IMAGE}", data = GetQrcodeImageBody(**params).json())
        return r.content

    def GetA8Key(self , **params) -> Dict:
        return self.post(WECHAT_GET_A8KEY , GetA8KeyBody(**params))

    def SendXml(self , **params) -> Dict:
        return self.post(WECHAT_MSG_SEND_XML , SendXmlBody(**params))

    def LogOut(self , **params) -> Dict:
        return self.post(WECHAT_LOGOUT , LogOutBody(**params))

    def GetTransfer(self , **params) -> Dict:
        return self.post(WECHAT_GET_TRANSFER , GetTransferBody(**params))

    def SendEmotion(self , **params) -> Dict:
        return self.post(WECHAT_MSG_SEND_EMOTION , SendEmotionBody(**params))

    def GetCdn(self , **params) -> Dict:
        return self.post(WECHAT_GET_CDN , GetCdnBody(**params))

    #[自定义
    def GetDBHandle(self, db_name="MicroMsg.db") -> int:
        if not self.db_handle:
            self.db_handle = {i["db_name"]: i["handle"] for i in self.GetDatabaseHandles()["data"]}

        return self.db_handle[db_name]

    def GetContactListBySql(self) -> Dict:
        sql = "select UserName,Alias,Remark,NickName,Type from Contact"   #  where type!=4 and type!=0;
        ContactList = self.QueryDatabase(db_handle=self.GetDBHandle(), sql=sql)["data"]
        contact_data = {}         # {wxid : {alias, remark, nickname , type}}
        for index in range(1, len(ContactList)):
            wxid = ContactList[index][0]
            contact_data[wxid] = {}
            contact_data[wxid]['alias'] = ContactList[index][1]
            contact_data[wxid]['remark'] = ContactList[index][2]
            contact_data[wxid]['nickname'] = ContactList[index][3]
            contact_data[wxid]['type'] = ContactList[index][4]

        sql = "select UserName,'' as Alias,Remark,NickName,Type from OpenIMContact"   #  where type!=4 and type!=0;
        OpenIMContactList = self.QueryDatabase(db_handle=self.GetDBHandle("OpenIMContact.db"), sql=sql)["data"]
        for index in range(1, len(OpenIMContactList)):
            wxid = OpenIMContactList[index][0]
            contact_data[wxid] = {}
            contact_data[wxid]['alias'] = ContactList[index][1]
            contact_data[wxid]['remark'] = OpenIMContactList[index][2]
            contact_data[wxid]['nickname'] = OpenIMContactList[index][3]
            contact_data[wxid]['type'] = OpenIMContactList[index][4]
        return contact_data

    def GetAllGroupMembersBySql(self) -> Dict:
        group_data = {} #{"group_id" : { "wxID" : "displayName"}}
        sql = "select ChatRoomName,RoomData from ChatRoom"
        GroupMemberList = self.QueryDatabase(db_handle=self.GetDBHandle(), sql = sql)['data']
        chatroom = ChatRoom.ChatRoomData()
        for index in range(1 , len(GroupMemberList)):
            group_member = {}
            chatroom.ParseFromString(bytes(base64.b64decode(GroupMemberList[index][1])))
            for k in chatroom.members:
                if k.displayName != "":
                    group_member[k.wxID] = k.displayName
            group_data[GroupMemberList[index][0]] = group_member
        return group_data

    def GetPictureBySql(self, wxid) -> Dict:
        if not wxid.endswith("@openim"):
            sql = f"select usrName,smallHeadImgUrl,bigHeadImgUrl from ContactHeadImgUrl where usrName='{wxid}';" 
            result = self.QueryDatabase(db_handle=self.GetDBHandle(),sql=sql)
        else:
            sql = f"select UserName,SmallHeadImgUrl,BigHeadImgUrl from OpenIMContact where UserName='{wxid}';" 
            result = self.QueryDatabase(db_handle=self.GetDBHandle("OpenIMContact.db"),sql=sql)
        try:
            if result["data"][1][2] != "":
                return result["data"][1][2]
            if result["data"][1][1] != "":
                return result["data"][1][1]
            return None
        except:
            return None

    def GetContactBySql(self, wxid):
        if not wxid.endswith("@openim"):
            sql = f"select UserName,Alias,Remark,NickName,Type from Contact where UserName='{wxid}';" 
            result = self.QueryDatabase(db_handle=self.GetDBHandle(),sql=sql)
        else:
            sql = f"select UserName,'' as Alias,Remark,NickName,Type from OpenIMContact where UserName='{wxid}';" 
            result = self.QueryDatabase(db_handle=self.GetDBHandle("OpenIMContact.db"),sql=sql)
        if len(result["data"]) > 0:
            return result["data"][1]
        else:
            return None
    #自定义]

    def post(self , type : int, params : Body) -> Dict:
        return json.loads(requests.post( f"http://127.0.0.1:{self.port}/api/?type={type}", data = params.json()).content.decode("utf-8"),strict=False)

    def exec_command(self , item: str) -> Callable:
        return eval(f"self.{item}")

        
