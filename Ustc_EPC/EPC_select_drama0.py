from EPC_select import select_lesson
import re
import time
import threading
import queue

class select_drama(select_lesson):
    def capture_key(self):
        f=self.Bhtml.find('form',{'action':re.compile("m_practice.asp?")}) #寻找所有action中带有m_practice.asp?的form
        self.list.append(f.get('action'))
        if not re.search(r'预约时间未到',f.get_text()):
            return True
        else:
            print('无课可选')
            return False

    def creat_thread(self,data):
        for i in range(1): # 从list中获取地址，创建线程
            url="http://epc.ustc.edu.cn/"+self.list[i]
            t=threading.Thread(target=self.post_html,args=(url,data))
            self.Theard.append(t)
        self.list.clear()

def check_login(iAi,q):
    while True:
        time.sleep(20)
        if not iAi.judge_login() or not q.empty():
            q.put(1)
            break

def main():
    datas={
    'submit_type':'book_submit'
    }
    iAi=select_drama('http://epc.ustc.edu.cn/m_practice.asp?second_id=2004')
    iAi.judge_login()

    q=queue.Queue()
    t=threading.Thread(target=check_login,args=(iAi,q))
    t.start()

    while True:
        if iAi.capture_key():
            iAi.creat_thread(datas)
            iAi.select_les()
            print("")
            break
        time.sleep(20)
        if not q.empty():
            break

    q.put(1)
    time.sleep(20)
    input("ENTER") # 按回车后退出

if __name__=="__main__":
    main()
