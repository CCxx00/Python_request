import itchat
import json

@itchat.msg_register(itchat.content.ATTACHMENT)
def reply_msg(msg):
    print(msg.text)

def main():
    itchat.auto_login(hotReload=True,enableCmdQR=True)
    # mpsList=itchat.get_mps(update=True)[1:]
    mpsList=itchat.search_mps(name='新闻早餐')
    for it in mpsList:
        print(it['NickName']+':'+it['Signature'])

    # itchat.run()
    # mpsList=itchat.get_chatrooms(update=True)[1:]
    mpsList=itchat.search_chatrooms(name='test')
    for it in mpsList:
        print(it['NickName'])
    #显示所有的群聊，包括未保存在通讯录中的，如果去掉则只是显示在通讯录中保存的
    itchat.dump_login_status()

    itchat.run()

if __name__=='__main__':
    main()
