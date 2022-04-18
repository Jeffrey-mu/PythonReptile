# 三方模块 需要安装
from webbrowser import get
import requests
url = 'https://fanyi.baidu.com/sug'
# get
# 指定设备
doc = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'})
print(doc.text)
doc.close()
s = input('请输入')
# post
dat = {
    "kw": s
}
docPost = requests.post(url, data=dat)
# 解析为json数据
print(docPost.json())
docPost.encoding = 'utf-8'
file = open('./1.json', mode='w')
file.writelines(docPost.text)
file.close()
# 关掉请求
docPost.close()