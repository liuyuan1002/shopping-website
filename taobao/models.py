from django.db import models

# Create your models here.

class User_cart(models.Model):
    username = models.CharField('用户名',max_length=50)
    total = models.IntegerField('总计',default=0)
    num = models.IntegerField('商品数量',default=0)

    def __str__(self):
        return self.username

class goods(models.Model):
    category = models.IntegerField('分类',default=0)
    goods_id = models.CharField('商品ID',max_length=10)
    goods_name = models.CharField('商品名',max_length=100,default='')
    goods_price = models.DecimalField('商品价格',max_digits=10,decimal_places=2)
    goods_Stock = models.IntegerField('商品库存',default=100)
    sales_Volume = models.IntegerField('销量',default=0)
    goods_introduce = models.CharField('商品简介',max_length=250,default='')
    def __str__(self):
        return self.goods_name

class cartItem(models.Model):
    quantuty = models.IntegerField('商品数量',default=1)
    unit_price = models.DecimalField('单价',max_digits=10,decimal_places=2)
    goods = models.ForeignKey(goods,default=None)
    username = models.CharField('用户名',max_length=50,default='')
    sum = models.DecimalField('总计',max_digits=10,decimal_places=2)
    def __str__(self):
        return self.username