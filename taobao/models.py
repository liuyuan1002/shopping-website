from django.db import models

# Create your models here.

class User_cart(models.Model):
    username = models.CharField(max_length=50)
    total = models.IntegerField(default=0)
    num = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username

class goods(models.Model):
    category = models.IntegerField(default=0)
    goods_id = models.CharField(max_length=10)
    goods_name = models.CharField(max_length=100,default='')
    goods_price = models.DecimalField(max_digits=10,decimal_places=2)
    goods_Stock = models.IntegerField(default=100)
    sales_Volume = models.IntegerField(default=0)
    goods_introduce = models.CharField(max_length=250,default='')

class cartItem(models.Model):
    quantuty = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    goods_id = models.CharField(max_length=10)
    username = models.CharField(max_length=50,default='')
    sum = models.DecimalField(max_digits=10,decimal_places=2)

