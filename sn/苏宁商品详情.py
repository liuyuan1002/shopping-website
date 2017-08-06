import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json


class suning_detail():
    def __init__(self,keyword):
        self.keyword = keyword
        self.link = ''
        self.id = ''
        self.brand = ''
        self.title = ''
        self.price = ''
        self.judgeNum = ''
        self.bestJudgeNum = ''
        self.midJudgeNum = ''
        self.worstJudgeNum = ''
        self.shop_nature = 1 #自营0，商家1
        self.shop_id = 0
        self.csv_link = u'F:/sn/商品详情/'+ self.keyword + u'商品详情.csv'
        self.file = open(u"f:/sn/商品链接/" + self.keyword + u'苏宁商品的链接' + u".txt")

    def getShopUrl(self):
        list = ['keyword', 'link', 'id', 'shop_id', 'title', 'price', 'judgeNum', 'bestJudgeNum','midJudgeNum','worstJudgeNum','shop_nature']
        df = pd.DataFrame(columns=list)
        while 1:
            self.link = self.file.readline()
            if not self.link:
                df.to_csv(self.csv_link)
                break
            print('商品链接：' + str(self.link))

            # do something
            html = requests.get(self.link)
            self.soup = BeautifulSoup(html.text,'lxml')
            self.getId()
            self.getShopId()
            # self.getBrand()
            self.getTitle()
            self.getPrice()
            self.getJudgenum()
            # self.getShop()
            df = df.append({'keyword':self.keyword,
                            'link': self.link,
                            'id': self.id,
                            'shop_id':self.shop_id,
                            # 'brand': self.brand,
                            'title': self.title,
                            'price': self.price,
                            'judgeNum': self.judgeNum,
                            'bestJudgeNum': self.bestJudgeNum,
                            'midJudgeNum':self.midJudgeNum,
                            'worstJudgeNum':self.worstJudgeNum,
                            'shop_nature':self.shop_nature
                            }, ignore_index=True)
            print('------------------')

    def getId(self):
        #获取商品ID
        self.id = self.link[37:-6]
        print('商品ID：'+str(self.id))

    def getShopId(self):
        self.shop_id = self.link[26:-16]
        print('商店Id：'+str(self.shop_id))

    # 获取商品品牌
    def getBrand(self):
        self.brand = ''
        a = self.soup.find_all('a', id="brand_relevance")
        if(len(a)  != 0):
            for i in a[0].children:
                if (len(i.string) > 1):
                    self.brand = i.string
        print('商品品牌：'+str(self.brand))

    # 获取商品名称1
    def getTitle(self):
        title = self.soup.find_all('h1',id = 'itemDisplayName')[0]
        if len(title)>1:
            self.shop_nature = 0
            print('店铺属性:自营')
        else :
            print('店铺属性:店家')
        j = 0
        for i in title:
            j+=1
            if self.shop_nature == 0 and j!=3:
                continue
            self.title = i.string.strip()
        print('商品名称：'+str(self.title))

    # 获取商品价格1
    def getPrice(self):
        Price_link = 'http://pas.suning.com/nspcsale_0_000000000'+str(self.id)+'_000000000'+str(self.id)+'_'+str(self.shop_id)+'_160_732_7320101.html'
        Price = requests.get(Price_link).text
        Price = Price[7:-2]
        Price = json.loads((Price))
        self.price = Price['data']['price']['saleInfo'][0]['promotionPrice']
        print(self.price)

    #商品评价详情
    def getJudgenum(self):
        juglink = 'http://review.suning.com/ajax/review_satisfy/general-000000000'+str(self.id)+'-'+str(self.shop_id)+'-----satisfy.htm?callback=satisfy'
        jug = requests.get(juglink).text
        jug = jug[8:-1]
        jug = json.loads(jug)['reviewCounts'][0]
        self.judgeNum = jug['totalCount']
        self.bestJudgeNum = jug['fiveStarCount'] + jug['fourStarCount']
        self.midJudgeNum = jug['threeStarCount'] + jug['twoStarCount']
        self.worstJudgeNum = jug['oneStarCount']
        print('评价总数：'+str(self.judgeNum))
        print('好评数：'+str(self.bestJudgeNum))
        print('中评数：'+str(self.midJudgeNum))
        print('差评数：'+str(self.worstJudgeNum))

    #店家
    def getShop(self):
        self.shop_nature = 0
        a = self.soup.find_all('p', class_='key_shop')
        if a:
            self.shop_nature = 1
            print('店家属性：' + '店家')

            shop_id_link = 'http://gps.yhd.com/restful/detail?mcsite=1&provinceId=1&pmId=' + self.id
            self.shop_id = requests.get(shop_id_link).json()['currentMerchantId']
            self.shop_link = 'http://shop.yhd.com/m-'+self.shop_id+'.html'

            shop_kpi_link = 'http://shop.yhd.com/kpi/'+self.shop_id
            html = requests.get(shop_kpi_link)
            soup = BeautifulSoup(html.text, 'lxml')
            a = soup.find_all('dd')

        else:
            print('店家属性：' + '自营')


if __name__ == '__main__':
    print("请输入关键字：")
    keyword = input()
    yhd = suning_detail(keyword)
    yhd.getShopUrl()


