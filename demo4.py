import itchat
import json

def auto_send(msg, toUser):
    itchat.send(msg=msg, toUserName=toUser)

if __name__ == "__main__":
    # itchat.login()
    itchat.auto_login(hotReload=True)
    #获取好友列表
    friends = itchat.get_friends()
    #转换为字典
    friendsStr = json.dumps(friends)
    # print(friendsStr)
    #发送消息
    # itchat.send(msg="你好", toUserName="8a30fa2addcac31cfe916506d80b2254")

    try:
        for item in friends:
            print(item["NickName"])
            if(item["NickName"] == "？！"):
                toUser = item["UserName"]
                auto_send('aaaa',toUser)
                itchat.run()
    except Exception as ex:
        itchat.logout()
        print(ex)
