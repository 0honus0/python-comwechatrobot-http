from typing import Callable, Any, Union, Awaitable , Optional , Dict
import requests
import json
from .Modles import *

class Api:
    port : int = 18888
    db_handle : int = 0

    def IsLoginIn(self , **params) -> bool:
        return self.post(WECHAT_IS_LOGIN , IsLoginBody(**params))

    def GetSelfInfo(self , **params):
        return self.post(WECHAT_GET_SELF_INFO , GetSelfInfoBody(**params))

    def SendText(self , **params):
        return self.post(WECHAT_MSG_SEND_TEXT , SendTextBody(**params))

    def SendAt(self , **params):
        return self.post(WECHAT_MSG_SEND_AT , SendAtBody(**params))

    def SendCard(self , **params):
        return self.post(WECHAT_MSG_SEND_CARD , SendCardBody(**params))

    def SendImage(self , **params):
        return self.post(WECHAT_MSG_SEND_IMAGE , SendImageBody(**params))

    def SendFile(**params):
        return self.post(WECHAT_MSG_SEND_FILE , SendFileBody(**params))
    
    def SendArticle(**params):
        return self.post(WECHAT_MSG_SEND_ARTICLE , SendArticleBody(**params))

    def SendApp(**params):
        return self.post(WECHAT_MSG_SEND_APP , SendAppBody(**params))

    def StartMsgHook(self, **params):
        return self.post(WECHAT_MSG_START_HOOK , StartMsgHookBody(**params))

    def StopMsgHook(self , **params):
        return self.post(WECHAT_MSG_STOP_HOOK , StopMsgHookBody(**params))
    
    def StartImageHook(self , **params):
        return self.post(WECHAT_MSG_START_IMAGE_HOOK , StartImageHookBody(**params))

    def StopImageHook(self , **params):
        return self.post(WECHAT_MSG_STOP_IMAGE_HOOK , StopImageHookBody(**params))

    def StartVoiceHook(self , **params):
        return self.post(WECHAT_MSG_STOP_VOICE_HOOK , StartVoiceHookBody(**params))

    def StopVoiceHook(self , **params):
        return self.post(WECHAT_MSG_STOP_VOICE_HOOK , StopVoiceHookBody(**params))

    def GetContactList(self , **params):
        return self.post(WECHAT_CONTACT_GET_LIST , GetContactListBody(**params))

    def CheckContactStatus(self , **params):
        return self.post(WECHAT_CONTACT_CHECK_STATUS , CheckContactStatusBody(**params))

    def DelContact(self , **params):
        return self.post(WECHAT_CONTACT_DEL , DelContactBody(**params))

    def SearchContactByCache(self , **params):
        return self.post(WECHAT_CONTACT_SEARCH_BY_CACHE , SearchContactByCacheBody(**params))

    def SearchContactByNet(self , **params):
        return self.post(WECHAT_CONTACT_SEARCH_BY_NET , SearchContactByNetBody(**params))

    def AddContactByWxid(self , **params):
        return self.post(WECHAT_CONTACT_ADD_BY_WXID , AddContactByWxidBody(**params))

    def AddContactByV3(self , **params):
        return self.post(WECHAT_CONTACT_ADD_BY_V3 , AddContactByV3Body(**params))

    def AddContactByPublicId(self , **params):
        return self.post(WECHAT_CONTACT_ADD_BY_PUBLIC_ID , AddContactByPublicIdBody(**params))

    def VerifyApply(self , **params):
        return self.post(WECHAT_CONTACT_VERIFY_APPLY , VerifyApplyBody(**params))

    def EditRemark(self , **params):
        return self.post(WECHAT_CONTACT_EDIT_REMARK , EditRemarkBody(**params))

    def GetChatroomMemberList(self , **params):
        return self.post(WECHAT_CHATROOM_GET_MEMBER_LIST , GetChatroomMemberListBody(**params))

    def GetChatroomMemberNickname(self , **params):
        return self.post(WECHAT_CHATROOM_GET_MEMBER_NICKNAME , GetChatroomMemberNicknameBody(**params))

    def DelChatroomMember(self , **params):
        return self.post(WECHAT_CHATROOM_DEL_MEMBER , DelChatroomMemberBody(**params))

    def AddChatroomMember(self , **params):
        return self.post(WECHAT_CHATROOM_ADD_MEMBER , AddChatroomMemberBody(**params))

    def SetChatroomAnnouncement(self , **params):
        return self.post(WECHAT_CHATROOM_SET_ANNOUNCEMENT , SetChatroomAnnouncementBody(**params))

    def SetChatroomName(self , **params):
        return self.post(WECHAT_CHATROOM_SET_CHATROOM_NAME , SetChatroomNameBody(**params))

    def SetChatroomSelfNickname(self , **params):
        return self.post(WECHAT_CHATROOM_SET_SELF_NICKNAME , SetChatroomSelfNicknameBody(**params))

    def GetDatabaseHandles(self , **params):
        return self.post(WECHAT_DATABASE_GET_HANDLES , GetDatabaseHandlesBody(**params))

    def BackupDatabase(self , **params):
        return self.post(WECHAT_DATABASE_BACKUP , BackupDatabaseBody(**params))

    def QueryDatabase(self , **params):
        return self.post(WECHAT_DATABASE_QUERY , QueryDatabaseBody(**params))

    def SetVersion(self , **params):
        return self.post(WECHAT_SET_VERSION , SetVersionBody(**params))

    def StartLogHook(self , **params):
        return self.post(WECHAT_LOG_START_HOOK , StartLogHookBody(**params))

    def StopLogHook(self , **params):
        return self.post(WECHAT_LOG_STOP_HOOK , StopLogHookBody(**params))

    def OpenBrowserWithUrl(self , **params):
        return self.post(WECHAT_BROWSER_OPEN_WITH_URL , OpenBrowserWithUrlBody(**params))

    def GetPublicMsg(self , **params):
        return self.post(WECHAT_GET_PUBLIC_MSG , GetPublicMsgBody(**params))

    def ForwardMessage(self , **params):
        return self.post(WECHAT_MSG_FORWARD_MESSAGE , ForwardMessageBody(**params))

    def GetQrcodeImage(self , **params):
        return self.post(WECHAT_GET_QRCODE_IMAGE , GetQrcodeImageBody(**params))

    #[自定义
    def GetDbHandle(self) -> Union[None, int]:
        try:
            return [i for i in json.loads(self.GetDatabaseHandles())["data"] if i["db_name"] == "MicroMsg.db"][0]["handle"] 
        except:
            return None

    def GetContactListBySql(self):
        if not self.db_handle:
            self.db_handle = self.GetDbHandle()
        sql = "select UserName,Alias,Remark,NickName from Contact" 
        return self.QueryDatabase(db_handle=self.db_handle,sql=sql)

    def GetPictureBySql(self):
        if not self.db_handle:
            self.db_handle = self.GetDbHandle()
        sql = "select usrName,bigHeadImgUrl from ContactHeadImgUrl" 
        return self.QueryDatabase(db_handle=self.db_handle,sql=sql)

    
    #自定义]

    def post(self , type : int, params : Body) -> Dict:
        return json.loads(requests.post( f"http://127.0.0.1:{self.port}/api/?type={type}", data = params.json()).text)

    def exec_command(self , item: str) -> Callable:
        return eval(f"self.{item}")

        