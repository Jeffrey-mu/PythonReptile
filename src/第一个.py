from urllib.request import urlopen
resp = urlopen('https://famobi.com/?locale=en')

with open('index.html', mode='w') as f:
    f.write(resp.read().decode('utf-8'))
    f.close()
print('结束')