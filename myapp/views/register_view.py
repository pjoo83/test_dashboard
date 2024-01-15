from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render


def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        count_user = User.objects.filter(username=username).count()
        if count_user > 0:
            code = 204
            message = '该用户已注册，请换个账号试试'
        else:
            user_profile = User()  # 实例话用户表
            user_profile.username = username
            user_profile.password = make_password(password)  # 对密码处理加密
            user_profile.email = email
            user_profile.is_active = 1
            user_profile.save()
            code = 200
            message = '注册成功，请登陆使用'
        return JsonResponse({"code": code, "message": message})
