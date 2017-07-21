

import requests
import re
import pymysql
import os
import time

def insertMysql(sql):
    config = {
              'host':'127.0.0.1',
              'port':3306,
              'passwd': "liuyuan",
              'user':'root',
              'db':'taobao',
              'charset':'utf8'
              }
    db = pymysql.connect(**config)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print(e)
    finally:
        cursor.close()
        db.close()


url = "http://www.ujipin.com/tag/cf845e092ec14640a904fa73d3c7eac9"
goodsUrl = []

a = requests.get(url).text
b = re.findall(r'href="/goods/([^?]*?)">',a)


for c in b:
    time.sleep(5)
    url = ( 'http://www.ujipin.com/goods/' + c)
    if os.path.exists(u'./static/images/goods/'+str(c)) == False:
        os.mkdir(u'./static/images/goods/'+str(c))

    html = requests.get(url).text
    #print(html)
    title = re.search(r'class="title">([^<]*?)</h4>',html).group(1)
    introduce = ''
    try:
        bb = re.search(r'\[(.*?)\](.*?)$',title)
        introduce = bb.group(1)
        title = bb.group(2)
    except Exception:
        introduce = ''

    price = re.search(r'data-price="(.*?)"', html).group(1)
    print(introduce)
    print(title)
    print(price)

    sql = 'INSERT INTO taobao_goods (category,goods_id,goods_price,goods_name,goods_introduce)  VALUES '
    sql = sql +  "({},'{}',{},'{}','{}');".format(
                1,
                str(c),
                float(price),
                title,
                introduce
                )
    insertMysql(sql)

    img = re.findall(r'data-original="([\s\S]*?)"', html)
    for i in range(0, len(img)):
        img[i] = img[i].replace('&amp;', '&')
    print(img[1])

    fileName = u'./static/images/goods/'+str(c)+'.jpg'
    jpg = requests.get(img[1]).content
    with open(fileName,'wb+') as  f:
        f.write(jpg)

    for i in range(1,len(img)):
        if(len(img[i]) > 200):
            continue
        fileName = u'./static/images/goods/' + str(c) + '/'+str(i)+'.jpg'
        jpg = requests.get(img[i]).content
        with open(fileName, 'wb+') as  f:
            f.write(jpg)







