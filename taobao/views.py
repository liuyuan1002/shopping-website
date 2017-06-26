from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from taobao.models import User,goods,cartItem
from .forms import UserForm
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import os


# Create your views here.
# def index(request):
#     return render(request,'base.html')

#注册
@csrf_exempt
def register(req):
    context = {'inputFormat':True,'userExit':False}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            #获得表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #添加到数据库

            if len(username) < 6 or len(password) < 6:
                context['inputFormat'] = False
                return render(req,'register.html',context)
            user = User.objects.filter(username=username)
            if user:
                context['userExit']=True
                return render(req, 'register.html', context)

            User.objects.create(username = username,password = password)
            req.session['username'] = username
            return redirect('/')
    else:
        context = {'isLogin':False}
    return  render(req,'register.html',context)


#登陆
@csrf_exempt
def login(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            #获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username = username,password = password)
            if user:
                #比较成功，跳转index
                req.session['username'] = username
                return redirect('/')
            else:
                #比较失败，还在login
                context = {'isLogin': False,'pawd':False}
                return render(req, 'login.html', context)
    else:
        context = {'isLogin': False,'pswd':True}
    return render(req, 'login.html', context)

#首页
def index(req):
    cc =  goods.objects.all().filter(category = 0)[:8]
    jf =  goods.objects.all().filter(category = 1)[:8]
    rm =  goods.objects.order_by('sales_Volume').all()[:8]

    context = {'cc':cc,'jf':jf,'rm':rm}

    username = ''
    if 'username' in req.session:
        username = req.session['username']
        context['isLogin'] = True
    else:
        context['isLogin'] = False
    context['username'] = username
    return render(req, 'index.html', context)

#退出
def logout(req):
    #清理cookie里保存username
    req.session.flush()
    return redirect('/')

def goodsDetail(req,goods_id):
    context={}

    if 'username' in req.session:
        username = req.session['username']

        context['isLogin'] = True
        context['username'] = username
    else:
        context['isLogin'] = False
    good = goods.objects.get(goods_id__exact=int(goods_id))

    context ['good'] = good
    len = 1
    urlImg = []
    while True:
        url = u'./static/images/goods/' + goods_id +'/'+str(len) + '.jpg'
        if os.path.exists(url) == False:
            break
        urlImg.append(url[1:])
        len += 1
    context['len'] = len
    context['urlImg'] = urlImg
    return  render(req,'goods.html',context)

def hot(req):
    rm = goods.objects.order_by('sales_Volume').all()[:36]
    context = {'rm':rm}
    username = ''
    if 'username' in req.session:
        username = req.session['username']
        context['isLogin'] = True
    else:
        context['isLogin'] = False
    context['username'] = username
    return render(req, 'hot.html', context)

def kitchen(req):
    cc = goods.objects.all().filter(category = 0)[:16]
    context = {'cc': cc}
    username = ''
    if 'username' in req.session:
        username = req.session['username']
        context['isLogin'] = True
    else:
        context['isLogin'] = False
    context['username'] = username
    return render(req, 'kitchen.html', context)

def home(req):
    jf = goods.objects.all().filter(category=1)[:16]
    context = {'jf': jf}
    username = ''
    if 'username' in req.session:
        username = req.session['username']
        context['isLogin'] = True
    else:
        context['isLogin'] = False
    context['username'] = username
    return render(req, 'homeTextiles.html', context)

def cart(req):
    context = {}
    username = ''
    if 'username' in req.session:
        username = req.session['username']
        context['isLogin'] = True
    else:
        context['isLogin'] = False
    context['username'] = username

    user = User.objects.get(username__exact=username)
    good = cartItem.objects.all().filter(username__exact = username)
    context['user'] = user
    context['good'] = good
    return render(req, 'cart.html', context)

def add_to_cart(req,goods_id,quantity):
    context = {'isLogin':True}
    username = ''
    if 'username' in req.session:
        username = req.session['username']
    else:
        context['isLogin'] = False

    good = goods.objects.get(goods_id__exact=goods_id)
    sum = int(quantity) * good.goods_price

    if cartItem.objects.all().filter(goods_id = goods_id):
        item = cartItem.objects.get(goods_id = goods_id)
        item.quantuty += int(quantity)
        item.sum += sum
        item.save()
    else:
        cartItem.objects.create(quantuty=quantity,unit_price=good.goods_price,goods_id= goods_id,username=username,sum = sum)


    use = User.objects.get(username=username)
    use.num += int(quantity)
    use.total += int(good.goods_price) * int (quantity)
    use.save()

    return  redirect('/')

def remove_from_cart(req,goods_id):
    context = {'isLogin': True}
    username = ''
    if 'username' in req.session:
        username = req.session['username']
    else:
        context['isLogin'] = False

    good = cartItem.objects.get(goods_id = goods_id,username = username)

    user = User.objects.get(username = username)

    user.num -= int(good.quantuty)
    user.total -=  int(good.unit_price) * int(good.quantuty)
    user.save()

    good.delete()
    return redirect('/cart/')

def search(req,keyword):
    good = goods.objects.filter(goods_introduce__contains=keyword)

    context = {'isLogin': True}
    username = ''
    if 'username' in req.session:
        username = req.session['username']
    else:
        context['isLogin'] = False
    context['username'] = username

    context['goods'] = good
    context['keyword'] = keyword

    return  render(req,'search.html',context)


