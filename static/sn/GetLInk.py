# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

class suning():
    def __init__(self,str):
        self.keyword = str
        self.pagenum = -1
        self.filename = u"f:/sn/商品链接/" + self.keyword + u'苏宁商品的链接' + u".txt"
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

if __name__ == '__main__':
    print ("请输入关键字：")
    keyword = input()
    tb = suning(keyword)

