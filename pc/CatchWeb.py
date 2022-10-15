import requests
import re
import os

image = "头像"
if not os.path.exists(image):
    os.mkdir(image)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
}
response = requests.get('https://www.woyaogexing.com/touxiang/weixin/2022/1274712.html', headers=headers)
response.encoding = "GBK"
response.encoding = "utf-8"
print(response.request.headers)
print(response.status_code)
t = '<img class="lazy" src="(.*?)">'
result = re.findall(t, response.text)

for img in result:
    str = 'https:' + img[0:62]
    print(str)