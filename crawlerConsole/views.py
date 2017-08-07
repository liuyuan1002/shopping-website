from django.shortcuts import render,redirect
from crawlerConsole.models import pcList

from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from django.contrib.auth.decorators import permission_required

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from dwebsocket import require_websocket

import json
import os
import re
# Create your views here.

from crawlerConsole.models import pcList
# from django_datatables_view.base_datatable_view import BaseDatatableView

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
    pclist = pcList.objects.all()
    context['pclist'] = pclist

    return render(req,'consoleIndex.html',context)

def error(req,index):
    if index == '403':
        return  HttpResponse(status=403)
    if index == '404':
        return HttpResponse(status=404)
    if index == '500':
        return  HttpResponse(status=500)

@csrf_exempt
def startCommand(req):
    if req.method == 'POST':
        ret = {'status': 1001, 'error': ''}
        pcid = req.POST.get('pcid',None)
        command = req.POST.get('command',None)

        pc = pcList.objects.get(id = pcid)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = BASE_DIR + pc.path


        # r = os.popen('python '+ path +' '+  command)
        r = os.system('python ' + path + ' ' + command)

        if pcid and command:
            ret['status'] = 1002
        else:
            ret['error'] = 'pcid or command error'
        return HttpResponse(json.dumps(ret))
    return redirect('/console/')


# @require_websocket
# def echo_once(req):
#     with open('cmdlog.txt', 'w+') as p:
#         req.websocket.send(p.readline())