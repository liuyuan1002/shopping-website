from django.contrib import admin
from . import  models
# Register your models here.

# admin.site.register(models.User)

admin.site.register(models.User_cart)
admin.site.register(models.goods)
admin.site.register(models.cartItem)