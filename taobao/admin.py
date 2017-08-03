from django.contrib import admin
from . import  models
# Register your models here.

# admin.site.register(models.User)

class goodsAdmin(admin.ModelAdmin):
    list_display = ['id','goods_name','goods_price','goods_Stock']

class user_cartAdmin(admin.ModelAdmin):
    list_display = ['id','username','num','total']

class cartItemAdmin(admin.ModelAdmin):
    list_display = ['id','username','goods_id','unit_price','quantuty']

admin.site.register(models.User_cart,user_cartAdmin)
admin.site.register(models.goods,goodsAdmin)
admin.site.register(models.cartItem,cartItemAdmin)