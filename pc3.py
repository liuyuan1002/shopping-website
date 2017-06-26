import requests
import re
import pymysql
import os
import time
goods_id = '13394'
len = 1
while True:
    url = './static/images/goods/' + goods_id + '/' + str(len) + '.jpg'
    print(url)
    if os.path.exists(url) == False:
        break
    len += 1

print(len)
