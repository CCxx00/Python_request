from bs4 import BeautifulSoup
import requests
import re
import time
import json

url_main='http://epc.ustc.edu.cn/'
url_record=url_main+'record_book.asp'
url_login=url_main+'n_left.asp'
url_topic=url_main+'m_practice.asp?second_id=2002'
url_drama=url_main+'m_practice.asp?second_id=2004'

def get_date(textname):
    with open(textname, 'r') as f:
        return json.loads(f.read()) #打开文件

def login(url,datas,headers):
    Session=requests.session()
    html=Session.post(url=url,data=datas,headers=headers)
    return Session

def get_choosed(url,Session):
    html=Session.get(url=url)
    html=BeautifulSoup(html.text,"html.parser")
    f=html.find_all('form',{'action':re.compile(r'record_book\.asp\?second')}) #寻找所有action中带有m_practice.asp?的form
    key_url=f[1].get('action')
    # print(key_url)
    key=f[1].find_all('td')
    key=re.search(r'[0-9]+',key[4].get_text()).group()
    # print(key)
    return key_url

def judge_login(url,Session):
    html=Session.get(url=url)
    html=BeautifulSoup(html.text,"html.parser")
    if(re.findall("登录后可以查看详细信息",html.get_text())): #寻找html页面中是否有登陆后。。。
        print("未登录")
        return 0
    else:
        # print("已登录")
        if check_lesson(html,Session)==9:
            return 9
        return 1

def check_lesson(html,Session):
    f=html.find_all('form',{'action':re.compile(r'm_practice\.asp\?second')})[0]
    key_url=f.get('action')
    key=f.find_all('td')
    key=re.search(r'[0-9]+',key[1].get_text()).group()
    f=f.get_text()
    if int(key)<13 and re.search(r'已达预约上限',f):
        cancel_lesson(get_choosed(url_record,Session),Session)
        choose_lesson(key_url,Session)
        return 9
    else:
        print('\rNo Lesson',end='')

def choose_lesson(key_url,Session):
    datas={
    'submit_type':'book_submit'
    }
    key_url=url_main+key_url
    print("开始选课:"+key_url)
    # str=BeautifulSoup(Session.post(url=key_url,data=datas).text,"html.parser") # 调用父类post_html(),比较返回值
    str=Session.post(url=key_url,data=datas).text
    if(re.findall("预约成功",str)):
        print("选课完成:"+key_url)
    elif(re.findall("操作失败：预约时间未到",str)):
        print("选课失败,预约时间未到")
    else:
        print("未知错误!")

def cancel_lesson(key_url,Session):
    datas={
    'submit_type':'book_cancel'
    }
    key_url=url_main+key_url
    Session.post(url=key_url,data=datas)

def main():
    headers=get_date('headers.txt')
    datas={
    'submit_type':'user_login',
    'name':'SA18011177',
    'pass':'zll1212hxe',
    'user_type':'2',
    'Submit':'LOG IN'
    }
    Session=login(url_login,datas,headers)
    count=0
    while True:
        key=judge_login(url_drama,Session)
        if key==9:
            break
        elif key==0:
            Session=login(url_login,datas,headers)
        print(count,end='')
        count+=1
        if count==1000:
            count=0
        time.sleep(10)

if __name__=='__main__':
    main()
