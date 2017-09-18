from taobao.models import goods

from django.http import JsonResponse
from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage

from django.views.decorators.csrf import  csrf_exempt

#分类展示
@csrf_exempt
def classify(req):
    context ={'status':200}
    type = req.POST.get('type','')
    page = req.POST.get('page','')

    context['type'] , context['page'] = type ,page
    if type == '0':
        goods_list = goods.objects.order_by('sales_Volume').all()
    else:
        goods_list = goods.objects.all().filter(category = int(type)).order_by('sales_Volume').all()

    if goods_list == None:
        return JsonResponse({'status':10021,'message':'parameter error'})

    paginator = Paginator(goods_list,8)
    try:
        goodss = paginator.page(int(page))
    except PageNotAnInteger:
        goodss = paginator.page(1)
    except EmptyPage:
        goodss = paginator.page(paginator.num_pages)

    context['queryNum'],context['hasPrevios'],context['hasNext'] = len(goodss),goodss.has_previous(),goodss.has_next()

    data = []

    if goodss:
        for i in goodss:
            good = {}
            good['goods_id'] = i.goods_id
            good['goods_name'] = i.goods_name
            good['goods_price'] = i.goods_price
            good['goods_stock'] = i.goods_Stock
            good['sales_volume'] = i.sales_Volume
            good['goods_introduce'] = i.goods_introduce
            data.append(good)
        context.update({'data':data})
        return JsonResponse(context)
    else:
        return  JsonResponse({'status':10022,'message':'query goods isempty'})


# return render(req,'classify.html',context)
# category = models.IntegerField('分类',default=0)
#     goods_id = models.CharField('商品ID',max_length=10)
#     goods_name = models.CharField('商品名',max_length=100,default='')
#     goods_price = models.DecimalField('商品价格',max_digits=10,decimal_places=2)
#     goods_Stock = models.IntegerField('商品库存',default=100)
#     sales_Volume = models.IntegerField('销量',default=0)
#     goods_introduce = models.CharField('商品简介',max_length=250,default='')