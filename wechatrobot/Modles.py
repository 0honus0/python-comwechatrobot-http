from pydantic.v1 import BaseModel

# login check
WECHAT_IS_LOGIN = 0                         # 登录检查

# self info
WECHAT_GET_SELF_INFO = 1                    # 获取个人信息

# send message
WECHAT_MSG_SEND_TEXT = 2                    # 发送文本
WECHAT_MSG_SEND_AT = 3                      # 发送群艾特
WECHAT_MSG_SEND_CARD = 4                    # 分享好友名片
WECHAT_MSG_SEND_IMAGE = 5                   # 发送图片
WECHAT_MSG_SEND_FILE = 6                    # 发送文件
WECHAT_MSG_SEND_ARTICLE = 7                 # 发送xml文章
WECHAT_MSG_SEND_APP = 8                     # 发送小程序

# receive message
WECHAT_MSG_START_HOOK = 9                   # 开启接收消息HOOK，只支持socket监听
WECHAT_MSG_STOP_HOOK = 10                   # 关闭接收消息HOOK
WECHAT_MSG_START_IMAGE_HOOK = 11            # 开启图片消息HOOK
WECHAT_MSG_STOP_IMAGE_HOOK = 12             # 关闭图片消息HOOK
WECHAT_MSG_START_VOICE_HOOK = 13            # 开启语音消息HOOK
WECHAT_MSG_STOP_VOICE_HOOK = 14             # 关闭语音消息HOOK

# contact
WECHAT_CONTACT_GET_LIST = 15                # 获取联系人列表
WECHAT_CONTACT_CHECK_STATUS = 16            # 检查是否被好友删除
WECHAT_CONTACT_DEL = 17                     # 删除好友
WECHAT_CONTACT_SEARCH_BY_CACHE = 18         # 从内存中获取好友信息
WECHAT_CONTACT_SEARCH_BY_NET = 19           # 网络搜索用户信息
WECHAT_CONTACT_ADD_BY_WXID = 20             # wxid加好友
WECHAT_CONTACT_ADD_BY_V3 = 21               # v3数据加好友
WECHAT_CONTACT_ADD_BY_PUBLIC_ID = 22        # 关注公众号
WECHAT_CONTACT_VERIFY_APPLY = 23            # 通过好友请求
WECHAT_CONTACT_EDIT_REMARK = 24             # 修改备注

# chatroom
WECHAT_CHATROOM_GET_MEMBER_LIST = 25        # 获取群成员列表
WECHAT_CHATROOM_GET_MEMBER_NICKNAME = 26    # 获取指定群成员昵称
WECHAT_CHATROOM_DEL_MEMBER = 27             # 删除群成员
WECHAT_CHATROOM_ADD_MEMBER = 28             # 添加群成员
WECHAT_CHATROOM_SET_ANNOUNCEMENT = 29       # 设置群公告
WECHAT_CHATROOM_SET_CHATROOM_NAME = 30      # 设置群聊名称
WECHAT_CHATROOM_SET_SELF_NICKNAME = 31      # 设置群内个人昵称

# database
WECHAT_DATABASE_GET_HANDLES = 32            # 获取数据库句柄
WECHAT_DATABASE_BACKUP = 33                 # 备份数据库
WECHAT_DATABASE_QUERY = 34                  # 数据库查询

# version
WECHAT_SET_VERSION = 35                     # 修改微信版本号

# log
WECHAT_LOG_START_HOOK = 36                  # 开启日志信息HOOK
WECHAT_LOG_STOP_HOOK = 37                   # 关闭日志信息HOOK

# browser
WECHAT_BROWSER_OPEN_WITH_URL = 38           # 打开微信内置浏览器
WECHAT_GET_PUBLIC_MSG = 39                  # 获取公众号历史消息

WECHAT_MSG_FORWARD_MESSAGE = 40             # 转发消息
WECHAT_GET_QRCODE_IMAGE = 41                # 获取二维码
WECHAT_GET_A8KEY = 42                       # 获取A8Key
WECHAT_MSG_SEND_XML = 43                    # 发送xml消息
WECHAT_LOGOUT = 44                          # 退出登录
WECHAT_GET_TRANSFER = 45                    # 收款
WECHAT_MSG_SEND_EMOTION = 46                # 发送表情
WECHAT_GET_CDN = 47                         # 下载文件、视频、图片

# Body

class Body(BaseModel):
    ...

#login check
class IsLoginBody(Body):
    ...

#self info
class GetSelfInfoBody(Body):
    ...

#send message
class SendTextBody(Body):
    wxid : str
    msg  : str

class SendAtBody(Body):
    chatroom_id  : str
    wxids        : str
    msg          : str
    auto_nickname: int = 1

class SendCardBody(Body):
    receiver   : str
    share_wxid : str
    nickname   : str

class SendImageBody(Body):
    receiver  : str
    img_path  : str

class SendFileBody(Body):
    receiver  : str
    file_path : str

class SendArticleBody(Body):
    wxid     : str
    title    : str
    abstract : str
    url      : str
    img_path : str

class SendAppBody(Body):
    wxid : str
    appid: str

#receive message
class StartMsgHookBody(Body):
    port : int

class StopMsgHookBody(Body):
    ...

class StartImageHookBody(Body):
    save_path : str

class StopImageHookBody(Body):
    ...

class StartVoiceHookBody(Body):
    save_path : str

class StopVoiceHookBody(Body):
    ...

#contact
class GetContactListBody(Body):
    ...

class CheckContactStatusBody(Body):
    wxid : str

class DelContactBody(Body):
    wxid : str

class SearchContactByCacheBody(Body):
    wxid : str

class SearchContactByNetBody(Body):
    keyword : str

class AddContactByWxidBody(Body):
    wxid : str
    msg  : str

class AddContactByV3Body(Body):
    v3       : str
    msg      : str
    add_type : int = 0x6

class AddContactByPublicIdBody(Body):
    public_id : str

class VerifyApplyBody(Body):
    v3 : str
    v4 : str

class EditRemarkBody(Body):
    wxid : str
    remark: str

#chatroom
class GetChatroomMemberListBody(Body):
    chatroom_id : str

class GetChatroomMemberNicknameBody(Body):
    chatroom_id : str
    wxid        : str

class DelChatroomMemberBody(Body):
    chatroom_id : str
    wxids       : str   # split by ","

class AddChatroomMemberBody(Body):
    chatroom_id : str
    wxids       : str   # split by ","

class SetChatroomAnnouncementBody(Body):
    chatroom_id : str
    announcement: str

class SetChatroomNameBody(Body):
    chatroom_id   : str
    chatroom_name : str

class SetChatroomSelfNicknameBody(Body):
    chatroom_id : str
    nickname    : str

#database
class GetDatabaseHandlesBody(Body):
    ...

class BackupDatabaseBody(Body):
    db_handle : str
    save_path : str

class QueryDatabaseBody(Body):
    db_handle : str
    sql       : str

#version
class SetVersionBody(Body):
    version : str  # "3.7.0.30"

#log
class StartLogHookBody(Body):
    ...

class StopLogHookBody(Body):
    ...

#browser
class OpenBrowserWithUrlBody(Body):
    url : str

class GetPublicMsgBody(Body):
    public_id : str
    offset    : str

#forward message
class ForwardMessageBody(Body):
    wxid  : str
    msgid : str

#qrcode
class GetQrcodeImageBody(Body):
    ...

#a8key
class GetA8KeyBody(Body):
    url : str

#send xml
class SendXmlBody(Body):
    wxid     : str
    xml      : str
    img_path : str

#logout
class LogoutBody(Body):
    ...

#get transfer
class GetTransferBody(Body):
    wxid          : str
    transcationid : str
    transferid    : str

#send emotion
class SendEmotionBody(Body):
    wxid     : str
    img_path : str

#get cdn
class GetCdnBody(Body):
    msgid : int
