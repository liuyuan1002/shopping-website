from django.shortcuts import render,redirect

from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.contrib.auth.decorators import permission_required

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

#判断是否登录
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


def login_view(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            # 获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = authenticate(username=username, password=password)
            if user:
                # 比较成功，跳转index
                auth.login(req, user)
                req.session['username'] = username
                return redirect('/console/')
            else:
                # 比较失败，还在login
                context = {'isLogin': False, 'pawd': False}
                return render(req, 'consoleLogin.html', context)
    else:
        context = {'isLogin': False, 'pswd': True}
    return render(req, 'consoleLogin.html', context)


@login_required(login_url='/console/login')
@permission_required('crawlerConsole.add_pclist',login_url='/error/403')
def index(req):
    context = user_session(req)
    return render(req,'consoleIndex.html',context)

def error(req,index):
    if index == '403':
        return  HttpResponse(status=403)
    if index == '404':
        return HttpResponse(status=404)
    if index == '500':
        return  HttpResponse(status=500)