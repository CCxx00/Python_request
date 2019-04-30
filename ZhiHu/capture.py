import sys
sys.path.append('../Ustc_EPC') # 父路径，./当前路径
from EPC_checkcode import internet_Ai
from bs4 import BeautifulSoup
import re
import time
import imghdr
import os

class zhihu(internet_Ai):
    def __init__(self,url,headers,cookies):
        super().__init__(url)
        self.cookies=cookies
        self.headers=headers

    def get_html(self,get_url,num):
        html=self.Session.get(url=get_url,headers=self.headers,cookies=self.cookies) #用get方法获取网页源代码
        count=0
        for i in html.json().get('data'):
            a=BeautifulSoup(i.get('content'),"html.parser")
            for b in a.find_all('noscript'):
                c=b.find('img')['src']
                print(c)
                image_name=re.split(r'/',c)[4]
                src='./image/'+str(num)+'_'+str(count)+'.jpg'
                # src='./image/'+image_name
                with open(src,'wb') as f:
                    f.write(self.Session.get(c).content) #保存目标地址的图片到image
                for d in range(10):
                    if not imghdr.what(src):
                        with open(src,'wb') as f:
                            f.write(self.Session.get(c).content) #保存目标地址的图片到image
                    else:
                        break
                if not imghdr.what(src):
                    os.remove(src)
                count+=1
                time.sleep(2)

def main():
    headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'referer':'https://www.zhihu.com/question/292901966'
    }
    cookies={
    r'_zap':r'50609046-6667-4b70-b2e4-d508d9a08314; _xsrf=eCtUIvjD5Y8Tzd5RiYEd4Lsrviu7d8qY',
    r'd_c0':r'"AJBiuoMRow6PTjBb9Id5NqtMSQjYpzWQawQ=|1544241504"',
    r'z_c0':r'"2|1:0|10:1551011376|4:z_c0|92:Mi4xS2FPTkF3QUFBQUFBa0dLNmd4R2pEaVlBQUFCZ0FsVk5NTnhmWFFBX1NFQjQ1OU9CNzZ5SDVPbUpFRzEtdGVaU093|0da4baf45f9fb51a1567038752cd948a5752367e1ee4b654b7589cbf1ee01179"',
    r'tgw_l7_route':r'116a747939468d99065d12a386ab1c5f',
    r'q_c1':r'7a6c39b52c6b4e70bd3f724a1da6d8be|1554126133000|1544241562000',
    'tst':'r'
    }
    a=zhihu('https://www.zhihu.com/api/v4/questions/30460976/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=0&platform=desktop&sort_by=default',headers,cookies)
    for i in range(100):
        a.get_html('https://www.zhihu.com/api/v4/questions/30460976/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset='+str(i*5)+'&platform=desktop&sort_by=default',i)

if __name__=='__main__':
    main()
