# author 刘源
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse
import urllib.request
import re
import datetime
import json
import sys
import os
import pymysql
import csv
import time



def add_log(content):
    pass
    # spider = "suning"
    # 上面改成自己爬虫的标示符，拼音就行
    # url1 = "http://49.123.21.100:8098/ba/"
    # url = url1 + "add_log.php?spider={}&content={}"
    # url = url.format(spider,urllib.parse.quote(content))
    # try:
    #     ws1 = urllib.request.urlopen(url).read()
    # except:
    #    return False
    # html = ws1.decode('utf-8')
    # if html == "1":
    #     return True
    # else:
    #     return False
#
#


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
            dict['goods_price'] = isNull(line[4])
            dict['goods_judge_num'] = isNull(line[5])
            dict['bestJudgeNum'] = isNull(line[6])
            dict['midJudgeNum'] = isNull(line[7])
            dict['worstJudgeNum'] = isNull(line[8])
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
    finally:
        cursor.close()
        db.close()

class suning_detail():
    def __init__(self,keyword):
        self.keyword = keyword
        self.goods_url = ''

        self.itemid = ''
        self.shopid = 0 #0为自营
        self.shop_nature = 0  #0为自营

        self.goods_title = ''
        self.goods_price = ''
        self.goods_judge_num = ''
        self.bestJudgeNum = ''
        self.midJudgeNum = ''
        self.worstJudgeNum = ''
        self.goods_addr='1'
        self.grab_time=''

        self.impressions = ''

        self.shopTitle = ''
        self.shop_url = ''
        self.shop_describe = ''
        self.shop_serve = ''
        self.shop_shipping = ''

        if os.path.exists(u'./商品详情') == False:
            os.mkdir(u'./商品详情')

        if os.path.exists(u'./商品链接') == False:
            os.mkdir(u'./商品链接')

        if os.path.exists(u'./商品详情/'+ self.keyword) == False:
            os.mkdir(u'./商品详情/'+ self.keyword)

        self.BaseInfoLink = u'./商品详情/'+ self.keyword + u'/BaseInfo.csv'
        self.ImpressionInfoLink = u'./商品详情/'+ self.keyword + u'/ImpressionInfo.csv'
        self.ShopInfoLink = u'./商品详情/' + self.keyword + u'/' u'/ShopInfo.csv'
        self.CommentInfoLink = u'./商品详情/' + self.keyword + u'/'+ u'/CommentInfo.csv'

        self.file = open(u"./商品链接/" + self.keyword + u".txt")

    def creatTable(self):
        list = ['itemid',
                'shopid',
                'goods_title',
                'goods_price',
                'goods_judge_num',
                'bestJudgeNum',
                'midJudgeNum',
                'worstJudgeNum',
                'goods_addr',
                'goods_url',
                'grab_time'
                ]
        self.BaseInfo = pd.DataFrame(columns=list)

        list = [
            'itemid',
            'impressions',
            'grab_time'
        ]
        self.ImpressionInfo = pd.DataFrame(columns=list)

        list = [
            'itemid',
            'shopid',
            'shopTitle',
            'shop_url',
            'shop_describe',
            'shop_serve',
            'shop_shiping',
            'grab_time'
        ]
        self.ShopInfo = pd.DataFrame(columns=list)

        list = [
            'itemid',
            'shopid',
            'id',
            'rateContent',
            'rateDate',
            'grab_time'
        ]
        self.CommentInfo = pd.DataFrame(columns=list)

    def saveTable(self):
        self.BaseInfo.to_csv(self.BaseInfoLink)
        self.ImpressionInfo.to_csv(self.ImpressionInfoLink)
        self.ShopInfo.to_csv(self.ShopInfoLink)
        self.CommentInfo.to_csv(self.CommentInfoLink)

    def getShopUrl(self):
        self.creatTable()
        while 1:
            time.sleep(5)
            self.goods_url = self.file.readline().replace('\n', ' ')
            if not self.goods_url:
                self.saveTable()
                self.file.close()
                break
            print('商品链接：' + str(self.goods_url))

            self.getId()
            self.grab_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace('\n', ' ')

            # do something
            try:
                self.html = requests.get(self.goods_url).text
                self.soup = BeautifulSoup(self.html,'lxml')
            except Exception:
                add_log(str(self.itemid) + ' '+ str(self.goods_url) + ' Error')


            self.getTitle()
            self.getPrice()
            self.getShop()
            self.getJudgenum()
            self.getCommentInfo()
            self.BaseInfo = self.BaseInfo.append({
                            'itemid': self.itemid,
                            'shopid': self.shopid,
                            'goods_title': self.goods_title,
                            'goods_price': self.goods_price,
                            'goods_judge_num': self.goods_judge_num,
                            'bestJudgeNum': self.bestJudgeNum,
                            'midJudgeNum': self.midJudgeNum,
                            'worstJudgeNum': self.worstJudgeNum,
                            'goods_addr': self.goods_addr,
                            'goods_url': self.goods_url,
                            'grab_time': self.grab_time
                            }, ignore_index=True)

            self.ImpressionInfo = self.ImpressionInfo.append({
                'itemid': self.itemid,
                'impressions': self.impressions,
                'grab_time': self.grab_time
            },ignore_index=True)

            self.ShopInfo = self.ShopInfo.append({
                'itemid': self.itemid,
                'shopid': self.shopid,
                'shopTitle': self.shopTitle,
                'shop_url': self.shop_url,
                'shop_describe': self.shop_describe,
                'shop_serve': self.shop_serve,
                'shop_shiping': self.shop_shipping,
                'grab_time': self.grab_time
            },ignore_index=True)

    def getId(self):
        #获取商品ID

        self.shopid = re.search('com/(.*?)/',self.goods_url).group(1)
        self.itemid = re.search('com/.*?/(.*?)\.html',self.goods_url).group(1)
        self.goods_url = 'http://product.suning.com/'+str(self.shopid)+'/'+str(self.itemid)+'.html'
        print('商店Id：' + str(self.shopid))
        print('商品ID：'+str(self.itemid))

    # 获取商品名称1
    def getTitle(self):
        try:
            self.goods_title = self.soup.select("title")[0].string.replace('\n', ' ')
        except Exception:
            pass
        print('商品名称：'+str(self.goods_title))

    # 获取商品价格1
    def getPrice(self):
        Price_link = 'http://pas.suning.com/nspcsale_0_000000000'+str(self.itemid)+'_000000000'+str(self.itemid)+'_'+str(self.shopid)+'_160_732_7320101.html'
        try:
            Price = requests.get(Price_link).text
            Price = Price[7:-2]
            Price = json.loads((Price))
            self.goods_price = Price['data']['price']['saleInfo'][0]['promotionPrice']
        except Exception:
            add_log(str(self.itemid) + ' getPrice Error' )
        print('goods_price:'+str(self.goods_price))

    # 店家
    def getShop(self):
        try:
            self.shopTitle= re.search('id=\"curShopName\">[\s\S]<a[\s\S]*?>([\s\S]*?)</a>', self.html).group(1)
            print(self.shopTitle)
        except Exception:
            pass
        self.shop_url = 'http://shop.suning.com/'+str(int(self.shopid))+'/consoleIndex.html'

        if int(self.shopid) == 0:
            url = 'http://review.suning.com/ajax/getShopScore/0000000000-shopReviewScore.htm?callback=shopReviewScore'
            try:
                html = requests.get(url).text
                self.shop_describe = re.search('\"qualityStar\":\"(.*?)\",', html).group(1)
                self.shop_serve = re.search('\"attitudeStar\":\"(.*?)\",', html).group(1)
                self.shop_shipping = re.search('\"deliverySpeedStar\":\"(.*?)\",', html).group(1)
            except Exception:
                add_log(str(self.itemid) + '  getshop Error')
            print('shop_describe:' + str(self.shop_describe))
            print('shop_serve:' + str(self.shop_serve))
            print('shop_shipping:' + str(self.shop_shipping))
        else :
            url = 'http://shop.suning.com/jsonp/'+str(int(self.shopid))+'/shopinfo/shopinfo.html'
            try:
                html = requests.get(url).text
                self.shop_describe = re.search('\"Qstar\":\"(.*?)\",', html).group(1)
                self.shop_serve = re.search('\"Astar\":\"(.*?)\",', html).group(1)
                self.shop_shipping = re.search('\"Dstar\":\"(.*?)\",',html).group(1)
            except Exception:
                add_log(str(self.itemid) + '  getshop Error')
            print('shop_describe:'+str(self.shop_describe))
            print('shop_serve:' + str(self.shop_serve))
            print('shop_shipping:' + str(self.shop_shipping))

    #商品评价详情
    def getJudgenum(self):
        juglink = 'http://review.suning.com/ajax/review_satisfy/general-000000000'+str(self.itemid)+'-'+str(self.shopid)+'-----satisfy.htm?callback=satisfy'
        try:
            jug = requests.get(juglink).text
            jug = jug[8:-1]
            jug = json.loads(jug)['reviewCounts'][0]
            self.goods_judge_num = jug['totalCount']
            self.bestJudgeNum = jug['fiveStarCount'] + jug['fourStarCount']
            self.midJudgeNum = jug['threeStarCount'] + jug['twoStarCount']
            self.worstJudgeNum = jug['oneStarCount']
        except Exception:
            add_log(str(self.itemid) + ' getJudgenum Error')

        print('评价总数：'+str(self.goods_judge_num))
        print('好评数：'+str(self.bestJudgeNum))
        print('中评数：'+str(self.midJudgeNum))
        print('差评数：'+str(self.worstJudgeNum))

        self.impressions=''
        review_link = 'http://review.suning.com/ajax/getreview_labels/general-000000000'+str(self.itemid)+'-'+str(self.shopid)+'-----commodityrLabels.htm'

        try:
            html = requests.get(review_link).text
            a = re.findall('\"labelName\":\"(.*?)\",\"labelCnt\":(.*?)}', html)
            for i in a:
                self.impressions += i[0] + ':'+i[1] + '-'
            self.impressions = self.impressions[:-1]
        except Exception:
            add_log(str(self.itemid) + ' getimpressions Error')
        print('impressions:'+str(self.impressions))

    #商品评论详情
    def getCommentInfo(self):
        try:
            time.sleep(5)
            good_link = 'http://review.suning.com/ajax/review_lists/general-000000000'+str(int(self.itemid))+'-'+str(self.shopid)+'-good-1-timeSort-10-----reviewList.htm?callback=reviewList'
            html = requests.get(good_link).text
            goodgenral = re.findall('\"content\":\"(.*?)\",\"publishTime\":\"(.*?)\"', html)
            id = 1
            for i in goodgenral:
                self.addCommentInfo(id,i[0].replace('\n',''),i[1])
                id += 1
                print(i[0].replace('\n','') + i[1])

            normal_link='http://review.suning.com/ajax/review_lists/general-000000000'+str(int(self.itemid))+'-'+str(self.shopid)+'-normal-1-timeSort-10-----reviewList.htm?callback=reviewList'
            html = requests. get(normal_link).text
            normalgenral = re.findall('\"content\":\"(.*?)\",\"publishTime\":\"(.*?)\"', html)
            id = 1
            for i in normalgenral:
                self.addCommentInfo(id, i[0].replace('\n',''), i[1])
                id += 1
                print(i[0].replace('\n','') + i[1])

            bad_link = 'http://review.suning.com/ajax/review_lists/general-000000000' + str(int(self.itemid)) + '-' + str(self.shopid) + '-bad-1-timeSort-10-----reviewList.htm?callback=reviewList'
            html = requests.get(bad_link).text
            badgenral = re.findall('\"content\":\"(.*?)\",\"publishTime\":\"(.*?)\"', html)
            id = 1
            for i in badgenral:
                self.addCommentInfo(id, i[0].replace('\n',''), i[1])
                id += 1
                print(i[0].replace('\n','') + i[1])
        except Exception:
            add_log(str(self.itemid) + ' getCommentInfo Error')


    def addCommentInfo(self,id,content,time):
        self.CommentInfo = self.CommentInfo.append({
            'itemid': self.itemid,
            'shopid': self.shopid,
            'id': id,
            'rateContent': content,
            'rateDate': time,
            'grab_time': self.grab_time
        }, ignore_index=True)

class suning_link():
    def __init__(self,str):

        self.keyword = str
        add_log('suning爬虫 启动' + self.keyword)
        self.pagenum = -1
        self.filename = u"./商品链接/" + self.keyword + u".txt"
        open(self.filename, 'w+')
        self.loop()

    def getNextUrl(self):
        '''该方法将返回一号店下一页，或者下拉加载的链接地址'''
        self.pagenum += 1
        return  'http://search.suning.com/emall/searchProductList.do?keyword='+str(self.keyword)+'&ci=0&pg=01&cp='+str(self.pagenum)

    def loop(self):
        """这个函数用于得到摸个一号店下面所有的链接"""
        tb2 = self.getNextUrl()
        print(tb2)
        html = requests.get(tb2).text

        while(html):
            soup = BeautifulSoup(html, 'lxml')
            a = soup.find_all('p', class_='sell-point')

            with open(self.filename, 'a') as p:
                for i in a:
                    p.write(i.a.get('href') + "\n")
                    print (i.a.get('href') + "\t\t")
            #内容为空则退出
            if(len(a)<1):
                break
            print(len(a))
            tb2 = self.getNextUrl()
            print(tb2)
            html = requests.get(tb2).text
        add_log('商品链接爬取成功')


if __name__ == '__main__':
    print("请输入关键字：")
    list = ['伊利qq星','伊利优酸乳','伊利味可滋','伊利安慕希',
            '伊利无菌砖','伊利纯牛奶','伊利舒化奶','伊利谷粒多',
            '伊利金典有机纯牛奶','特仑苏','甜小嗨','蒙牛奶特',
            '蒙牛新养道','蒙牛早餐奶','蒙牛纯牛奶','蒙牛纯甄',
            '蒙牛谷粒早餐']
    # keyword = input()
    # keyword = sys.argv[1]
    # suning_link(keyword)
    # suning = suning_detail(keyword)
    # suning.getShopUrl()
    for keyword in list:
        csvToMysql(keyword)


