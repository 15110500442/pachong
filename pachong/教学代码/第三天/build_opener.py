# 实质：urlopenn内部其实就是使用build_opener来创建了一个opener对象
# 最后将这个对象返回给我们

import urllib.request 
import http
import ssl
#urlopen内部的简单实现原理、流程
#https_handler = HTTPSHandler(context=context)
context = ssl._create_unverified_context()
#构建一个handler，支持发送https请求
https_handler = urllib.request.HTTPSHandler(context=context)
#创建一个opener
opener = urllib.request.build_opener(https_handler)
url = 'https://www.baidu.com'
response = opener.open(url)
req = urllib.request.Request(url)
response = opener.open(req)
print(response.code)


