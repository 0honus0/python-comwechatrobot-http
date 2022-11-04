```
from wechatrobot import WeChatRobot


bot = WeChatRobot()

@bot.on("friend_msg")
def on_friend_msg(msg):
    bot.SendText(wxid = msg['sender'], msg = msg['message'])

@bot.on("group_msg")
def on_group_msg(msg):
    print(f"on_group_msg: {msg}")

@bot.on("self_msg")
def on_self_msg(msg):
    print(f"on_self_msg: {msg}")

bot.run()
```
