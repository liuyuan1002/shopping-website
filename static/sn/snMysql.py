import csv
import pymysql

def insertMysql(sql):
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'passwd': "LIUyuan052013",
        'user': 'root',
        'db': 'sn1',
        'charset': 'utf8'
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

def csvToMysql( keyword):
    BaseInfoLink = u'./商品详情/' + keyword + u'/BaseInfo.csv'
    ImpressionInfoLink = u'./商品详情/' + keyword + u'/ImpressionInfo.csv'
    ShopInfoLink = u'./商品详情/' + keyword + u'/ShopInfo.csv'
    CommentInfoLink = u'./商品详情/' + keyword + u'/CommentInfo.csv'

    def isNull(string = 'null'):
        if len(str(string)) < 1:
            return str('null')
        else: return string

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

    with open(BaseInfoLink, "r") as csvfile:
        sql = 'INSERT INTO sn_baseinfo (itemId,shopid,goods_title,goods_price,goods_judge_num,bestJudgeNum,midJudgeNum,worstJudgeNum,goods_addr,goods_url,grab_time)  VALUES '
        # 读取csv文件，返回的是迭代类型
        read = csv.reader(csvfile)
        le = 0
        for line in read:
            # print(line)
            le += 1
            if le == 1:
                continue
            dict['itemid'] = line[1]
            dict['shopid'] = line[2]
            dict['goods_title'] = line[3]
            dict['goods_price'] = line[4]
            dict['goods_judge_num'] = line[5]
            dict['bestJudgeNum'] = line[6]
            dict['midJudgeNum'] = line[7]
            dict['worstJudgeNum'] = line[8]
            dict['goods_addr'] = line[9]
            dict['goods_url'] = line[10]
            dict['grab_time'] = line[11]

            sql = sql + "('{}','{}','{}',{},{},{},{},{},'{}','{}','{}'),".format(
                dict['itemid'],
            dict['shopid'],
            dict['goods_title'],
            dict['goods_price'] ,
            dict['goods_judge_num'] ,
            dict['bestJudgeNum'],
            dict['midJudgeNum'] ,
            dict['worstJudgeNum'],
            dict['goods_addr'] ,
            dict['goods_url'],
            dict['grab_time'] ,)
        if le != 1:
            insertMysql(sql[:-1] + ';')

    with open(ImpressionInfoLink, "r") as csvfile:
        sql = 'INSERT INTO sn_impressioninfo (itemId,impressions,grab_time)  VALUES '
        # 读取csv文件，返回的是迭代类型
        read = csv.reader(csvfile)
        le = 0
        for line in read:
            # print(line)
            le += 1
            if le == 1:
                continue
            dict['itemid'] = line[1]
            dict['impressions'] = line[2]
            dict['grab_time'] = line[3]
            sql = sql + "('{}','{}','{}'),".format(
                dict['itemid'],
                dict['impressions'],
                dict['grab_time'])
        if le != 1:
            insertMysql(sql[:-1] + ';')

    with open(ShopInfoLink, "r") as csvfile:
        sql = 'INSERT INTO sn_shopinfo (itemId,shopId,shopTitle,shop_url,shop_describe,shop_serve,shop_shipping,grab_time)  VALUES '
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
            dict['shopTitle'] = line[3]
            dict['shop_url'] = line[4]
            dict['shop_describe'] =isNull(line[5])
            dict['shop_serve'] = isNull(line[6])
            dict['shop_shipping'] = isNull(line[7])
            dict['grab_time'] = line[8]
            sql = sql + "('{}','{}','{}','{}',{},{},{},'{}'),".format(
                dict['itemid'],
                dict['shopId'],
                dict['shopTitle'],
                dict['shop_url'],
                dict['shop_describe'],
                dict['shop_serve'],
                dict['shop_shipping'],
                dict['grab_time'])
        if le != 1:
            insertMysql(sql[:-1] + ';')

    with open(CommentInfoLink, "r") as csvfile:
        sql = 'INSERT INTO sn_CommentInfo(itemId,shop_id,id,rateContent,rateDate,grab_time)  VALUES '
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
                dict['sellerId'],
                dict['id'],
                dict['rateContent'],
                dict['rateDate'],
                dict['grab_time'])
        if le != 1:
            insertMysql(sql[:-1] + ';')

if __name__ == '__main__':
    csvToMysql(keyword='甜小嗨')
