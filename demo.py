from urllib import request

url='https://www.lagou.com/'
url1='http://httpbin.org/ip'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# set proxy
handler=request.ProxyHandler({'http':'183.166.136.33:9999'})
opener=request.build_opener(handler)

# set request
req=request.Request(url1,headers=headers)
# get data of url 
# resp=request.urlopen(req)
resp=opener.open(req)
print(resp.read().decode('utf-8'))
