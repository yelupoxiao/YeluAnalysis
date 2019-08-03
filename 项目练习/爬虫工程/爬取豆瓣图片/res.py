import json
import re
import os
import requests

# 创建图片存储文档
query = '周星驰'
path = os.getcwd()
picpath = path + '/' + query # 图片存储位置文件夹
print(picpath)
if not os.path.isdir(picpath):  # 没有该文件夹则创建一个
    os.mkdir(picpath)


# 创建下载函数
def download(src, id):
    dir = picpath + '/' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
    except requests.exceptions.ConnectionError:
        print(id + '图片无法下载')
    fp = open(dir, 'wb')
    fp.write(pic.content)
    fp.close()


# 抓取图片地址与id
for i in range(0, 2000, 20):
    url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
    html = requests.get(url).text
    response = json.loads(html,encoding = 'uft-8')
    print('已下载' + str(i) + '张图片')
    for image in response['images']:
        image['src'] = image['src'].replace('thumb', 'l')
        print(image['src'])
        download(image['src'], image['id'])
