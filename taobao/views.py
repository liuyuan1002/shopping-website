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

from django.core.paginator import  Paginator ,EmptyPage,PageNotAnInteger
from django.db.models import Q


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
            User_cart.objects.create(username=username).save()

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

    next_to = req.GET.get('next-to', '/taobao/')
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
                return  redirect(next_to)
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
    cc =  goods.objects.all().filter(category = 1)[:8]
    jf =  goods.objects.all().filter(category = 2)[:8]
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

#分类展示
def classify(req,type,page):
    context = user_session(req)
    context['type'] = int(type)
    if type == '0':
        goods_list = goods.objects.order_by('sales_Volume').all()
    else:
        goods_list = goods.objects.all().filter(category = int(type))
    paginator = Paginator(goods_list,8)

    try:
        goodss = paginator.page(int(page))
    except PageNotAnInteger:
        goodss = paginator.page(1)
    except EmptyPage:
        goodss = paginator.page(paginator.num_pages)

    context['goods'] = goodss
    return render(req,'classify.html',context)

#查看购物车
@login_required(login_url='/taobao/login')
def cart(req):
    context = user_session(req)
    try:
        user = User_cart.objects.get(username__exact=context['username'])
        good = cartItem.objects.all().filter(username__exact = context['username'])
    except:
        user , good= None , None

    context['user'] = user
    context['good'] = good
    return render(req, 'cart.html', context)

#添加到购物车
@login_required(login_url='/taobao/login')
def add_to_cart(req,goods_id,quantity):
    context = user_session(req)

    good = goods.objects.get(goods_id__exact=goods_id)
    sum = int(quantity) * good.goods_price

    if cartItem.objects.all().filter(goods=good):
        item = cartItem.objects.get(goods=good)
        item.quantuty += int(quantity)
        item.sum += sum
        item.save()
    else:
        cartItem.objects.create(quantuty=quantity,unit_price=good.goods_price,goods=good,username=context['username'],sum = sum)


    use = User_cart.objects.get(username=context['username'])
    use.num += int(quantity)
    use.total += int(good.goods_price) * int (quantity)
    use.save()

    return  redirect('/taobao/cart/')

# https://docs.djangoproject.com/en/1.11/topics/auth/default/#the-login-required-decorator
@login_required(login_url='/taobao/login')
def remove_from_cart(req,goods_id):
    context = user_session(req)

    good = goods.objects.get(goods_id__exact=goods_id)
    good = cartItem.objects.get(goods = good,username = context['username'])

    user = User_cart.objects.get(username = context['username'])

    user.num -= int(good.quantuty)
    user.total -=  int(good.unit_price) * int(good.quantuty)
    user.save()

    good.delete()
    return redirect('/taobao/cart/')


def search_name(req):
    # good = goods.objects.filter(goods_introduce__contains=keyword)

    context = {'isLogin': True}
    username = ''
    if 'username' in req.session:
        username = req.session['username']
    else:
        context['isLogin'] = False
    context['username'] = username

    search_name = req.GET.get("name","")
    goods_list  = goods.objects.filter(Q(goods_introduce__icontains = search_name) | Q(goods_name__icontains = search_name))


    context['goods'] = goods_list
    context['keyword'] = search_name

    return  render(req,'search.html',context)


