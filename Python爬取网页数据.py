from urllib.request import urlopen
url = "https://www.baidu.com/"
# url = "要爬取网页的网址"
resp = urlopen(url)
print(resp.read)
# 如有乱码，可在print(resp.read()后添加.decode("utf-8/gbk"))，如：print(resp.read.decode("utf-8")) 或 print(resp.read.decode("gbk"))
