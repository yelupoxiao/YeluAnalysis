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