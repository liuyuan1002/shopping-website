from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext

from taobao.models import User_cart,goods,cartItem
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import os

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
# def index(request):
#     return render(request,'base.html')

#判断用户是否在session中
def user_session(req):
    context = {}
    if 'username' in req.session:
        username = req.session['username']
        context['isLogin'] = True
        context['username'] = username
    else:
        context['isLogin'] = False
        context['username'] = ''
    return context

#注册
@csrf_exempt
def register_view(req):
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

            user = auth.authenticate(username = username,password = password)
            if user:
                context['userExit']=True
                return render(req, 'register.html', context)

            user = User.objects.create_user(username=username, password=password)
            user.save()
            User_cart.objects.create(username=username)

            req.session['username'] = username
            auth.login(req, user)
            return redirect('/taobao/')
    else:
        context = {'isLogin':False}
    return  render(req,'register.html',context)

#登陆
@csrf_exempt
def login_view(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            #获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = authenticate(username = username,password = password)
            if user:
                #比较成功，跳转index
                auth.login(req,user)
                req.session['username'] = username
                return redirect('/taobao/')
            else:
                #比较失败，还在login
                context = {'isLogin': False,'pawd':False}
                return render(req, 'login.html', context)
    else:
        context = {'isLogin': False,'pswd':True}
    return render(req, 'login.html', context)

#首页
def index(req):
    context = user_session(req)
    cc =  goods.objects.all().filter(category = 0)[:8]
    jf =  goods.objects.all().filter(category = 1)[:8]
    rm =  goods.objects.order_by('sales_Volume').all()[:8]
    context['cc']= cc
    context['jf'] = jf
    context['rm'] = rm

    return render(req, 'index.html', context)

#退出
def logout_view(req):
    #清理cookie里保存username
    #req.session.flush()
    logout(req)
    return redirect('/taobao/')

def goodsDetail(req,goods_id):
    context = user_session(req)
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
    context = user_session(req)
    rm = goods.objects.order_by('sales_Volume').all()[:36]
    context['rm']=rm
    return render(req, 'hot.html', context)

def kitchen(req):
    context = user_session(req)
    cc = goods.objects.all().filter(category = 0)[:16]
    context['cc'] = cc
    return render(req, 'kitchen.html', context)

def home(req):
    context = user_session(req)
    jf = goods.objects.all().filter(category=1)[:16]
    context['jf'] = jf
    return render(req, 'homeTextiles.html', context)

@login_required
def cart(req):
    context = user_session(req)

    user = User_cart.objects.get(username__exact=context['username'])
    good = cartItem.objects.all().filter(username__exact = context['username'])
    context['user'] = user
    context['good'] = good
    return render(req, 'cart.html', context)

@login_required
def add_to_cart(req,goods_id,quantity):
    context = user_session(req)

    good = goods.objects.get(goods_id__exact=goods_id)
    sum = int(quantity) * good.goods_price

    if cartItem.objects.all().filter(goods_id = goods_id):
        item = cartItem.objects.get(goods_id = goods_id)
        item.quantuty += int(quantity)
        item.sum += sum
        item.save()
    else:
        cartItem.objects.create(quantuty=quantity,unit_price=good.goods_price,goods_id= goods_id,username=context['username'],sum = sum)


    use = User_cart.objects.get(username=context['username'])
    use.num += int(quantity)
    use.total += int(good.goods_price) * int (quantity)
    use.save()

    return  redirect('/taobao/')

@login_required
def remove_from_cart(req,goods_id):
    context = user_session(req)

    good = cartItem.objects.get(goods_id = goods_id,username = context['username'])

    user = User_cart.objects.get(username = context['username'])

    user.num -= int(good.quantuty)
    user.total -=  int(good.unit_price) * int(good.quantuty)
    user.save()

    good.delete()
    return redirect('/taobao/cart/')

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


