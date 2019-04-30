from EPC_select import select_lesson
from auSendMail import mail
import re
import time
import threading

class select_drama(select_lesson):
    def capture_key(self):
        f=self.Bhtml.find('form',{'action':re.compile("m_practice.asp?")}) #寻找所有action中带有m_practice.asp?的form
        self.list.append(f.get('action'))
        f=f.get_text()
        r=['llmxdxcb@gmail.com']
        M=mail('1375062160@qq.com','covpapiglbgmhdah',r)
        M.message_set('抢课','1375062160@qq.com','llmxdxcb@gmail')
        if re.search(r'预约时间未到',f):
            print('预约时间未到')
            return False
        elif re.search(r'已达预约上限',f):
            print('已达预约上限')
            M.send_mail()
            return True
        else:
            print(f)
            M.send_mail()
            return True

    def creat_thread(self,data):
        for i in range(1): # 从list中获取地址，创建线程
            url="http://epc.ustc.edu.cn/"+self.list[i]
            t=threading.Thread(target=self.post_html,args=(url,data))
            self.Theard.append(t)
        self.list.clear()

def main():
    datas={
    'submit_type':'book_submit'
    }
    iAi=select_drama('http://epc.ustc.edu.cn/m_practice.asp?second_id=2004')

    while True:
        if iAi.judge_login():
            if iAi.capture_key():
                iAi.creat_thread(datas)
                iAi.select_les()
                break
            time.sleep(5)
        else:
            break

    input("ENTER") # 按回车后退出

if __name__=="__main__":
    main()
