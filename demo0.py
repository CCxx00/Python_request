from urllib import request
from http.cookiejar import MozillaCookieJar

url='http://www.baidu.com/'
cookiejar=MozillaCookieJar('cookie.txt')
handler=request.HTTPCookieProcessor(cookiejar)
opener=request.build_opener(handler)
opener.open(url)
cookiejar.save(ignore_discard=True)
