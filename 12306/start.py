import requests
from bs4 import BeautifulSoup

'''
https://kyfw.12306.cn/otn/resources/merged/login_UAM_js.js?scriptVersion=1.9094:formatted
res = requests.get("https://kyfw.12306.cn/otn/index/init")
res = requests.get("https://kyfw.12306.cn/otn/resources/merged/index_end_js.js?scriptVersion=1.9094")
'''
#res = requests.get("https://kyfw.12306.cn/otn/login/init")
#res = requests.get("https://kyfw.12306.cn/otn/login/init")
#res = requests.get("https://kyfw.12306.cn/otn/login/userLogin")

res = requests.get("https://kyfw.12306.cn/otn/login/init")

res.encoding = "UTF-8"
print(type(res))
