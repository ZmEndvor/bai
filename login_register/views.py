import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def render_template_error_and_next(request, template):
    error_message = request.session.get('error_message')
    request.session['error_message'] = None
    next = request.GET.get('next', '')
    return render(request, template, {'error_message': error_message, 'next': next})


def login_html(request):
    return render_template_error_and_next(request, 'blog/signin.html')


@csrf_exempt
def signin_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    checkbox = request.POST.get('checkbox')
    if not checkbox:
        request.session.set_expiry(0)
    user = authenticate(username=username, password=password)
    if user:
        print('登录成功')
        # 将登陆的用户写入到session中
        login(request, user)
        # request.session['username'] = user.username
        next = request.POST.get('next')
        if not next:
            return JsonResponse({'err':0})
        else:
            return JsonResponse({'next':next})

    else:
        print('登录失败')
        # return render(request, 'login1.html', {'error_message': '用户名和密码错误!'})
        error_messae = '用户名或密码错误!'

    return JsonResponse({'err':1,'msg':error_messae})


def login_out(request):
    logout(request)
    request.session['username'] = ''
    return HttpResponseRedirect('/')


def register(request):
    return render_template_error_and_next(request, 'blog/register.html')


@csrf_exempt
def register_submit(request):
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    # 用正则表达式，对用户名和密码做有效性检测
    # 自行补充完成
    if re.match(r'^[a-zA-Z0-9_\-]{2,20}$', str(username)):
        if re.match(r'^[a-zA-Z0-9.]{2,20}$', str(password1)):
            if password1 and password1 == password2:
                try:
                    User.objects.create_user(username=username, password=password1)
                    return JsonResponse({'err':0})
                except IntegrityError as e:
                    error_message = '用户名已存在'
                    return JsonResponse({'err': 1, 'msg': error_message})
            else:
                error_message = '两次输入的密码不一样！'
                return JsonResponse({'err': 1, 'msg': error_message})

        else:
            error_message = '密码不符合规定！'
            return JsonResponse({'err': 1, 'msg': error_message})
    else:
        error_message = '用户名不符合规定！'
        # request.session['error_message'] = error_message
        return JsonResponse({'err': 1, 'msg': error_message})

def change_password(request):
    old_password = request.POST.get('old_password')
    new_password1 = request.POST.get('new_password1')
    new_password2 = request.POST.get('new_password2')

    user = authenticate(username=request.user.username, password=old_password)

    if user:
        # 设置新密码，会自动进行加密
        user.set_password(new_password1)
        user.save()


def validate_username(request):
    username = request.POST.get('username')
    l = User.objects.filter(username=username)
    if l:
        return JsonResponse({'error': 1})
    else:
        return JsonResponse({'error': 0})