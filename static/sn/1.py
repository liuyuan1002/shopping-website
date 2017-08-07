import csv
import pymysql
import os

def insertMysql(sql):
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'passwd': "liuyuan",
        'user': 'root',
        'db': 'sn',
        'charset': 'utf8'
    }
    db = pymysql.connect(**config)
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print(e)
        print(sql)
    finally:
        cursor.close()
        db.close()

BASE_PATH = os.path.dirname(__file__)
list = ['伊利qq星','伊利优酸乳','伊利味可滋','伊利安慕希',
            '伊利无菌砖','伊利纯牛奶','伊利舒化奶','伊利谷粒多',
            '伊利金典有机纯牛奶','特仑苏','甜小嗨','蒙牛奶特',
            '蒙牛新养道','蒙牛早餐奶','蒙牛纯牛奶','蒙牛纯甄',
            '蒙牛谷粒早餐']

dict = {'itemid': '',
            'shopid': '',
            'goods_title': '',
            'goods_price': '',
            'goods_judge_num': '',
            'bestJudgeNum': '',
            'midJudgeNum': '',
            'worstJudgeNum': '',
            'goods_addr': '',
            'grab_time': '',
            'goods_url': '',
            'impressions': '',
            'shopTitle': '',
            'shop_url': '',
            'shop_describe':'',
            'shop_serve':'',
            'shop_shipping':'',
            'id': '',
            'rateContent': '',
            'rateDate': ''
            }

for keyword in list:
    CommentInfoLink = BASE_PATH + u'/商品详情/' + keyword + u'/CommentInfo.csv'
    with open(CommentInfoLink, "r") as csvfile:
        sql = 'INSERT INTO sn_CommentInfo(itemId,sellerid,id,rateContent,rateDate,grab_time)  VALUES '
        # 读取csv文件，返回的是迭代类型
        read = csv.reader(csvfile)
        le = 0
        for line in read:
            # print(line)
            le += 1
            if le == 1:
                continue
            dict['itemid'] = line[1]
            dict['shopId'] = line[2]
            dict['id'] = line[3]
            dict['rateContent'] = line[4]
            dict['rateDate'] = line[5]
            dict['grab_time'] = line[6]

            sql = sql + "('{}','{}','{}','{}','{}','{}'),".format(
                dict['itemid'],
                dict['shopId'],
                dict['id'],
                dict['rateContent'],
                dict['rateDate'],
                dict['grab_time'])
        if le != 1:
            insertMysql(sql[:-1] + ';')

