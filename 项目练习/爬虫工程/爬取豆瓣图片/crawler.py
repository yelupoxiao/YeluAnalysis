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