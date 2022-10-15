import os.path
import time
import urllib.request

import requests
import re
import random
import _pyinstaller_hooks_contrib

image = "头像"
if not os.path.exists(image):
    os.mkdir(image)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Referer': 'https://www.wxcha.com/touxiang/update_1.html'
}
# ssl._create_default_https_context = ssl.create_default_context()
response = requests.get('https://www.wxcha.com/touxiang/78556.html', headers=headers)
response.encoding = "GBK"
response.encoding = "utf-8"
print(response.request.headers)
print(response.status_code)
t = '<li class=""><a href="(.*?)">'
result = re.findall(t, response.text)
i = 1
for src in result:
    # print(src)
    img = src.split("?")
    time.sleep(random.randint(5, 20))
    str1 = img[0]
    req = urllib.request.Request(str1, headers=headers)
    resp = urllib.request.urlopen(req)
    with open(image + "/" + str(i+1) + ".jpg", 'wb') as f:
        f.write(resp.read())
        i = i + 1
