from django import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True, min_length=3)


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        login_form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if login_form.is_valid():
            user = authenticate(username=username, password=password)
            if user:
                if user.is_staff:
                    # 权限装饰器，判断是否有权限可进入项目
                    login(request, user)
                    # 存入session，超时需登陆
                    request.session['info'] = {'id': request.POST.get('id'), 'name': username}
                    request.session.set_expiry(60 * 60 * 24)
                    return redirect('/autotest/index/')
                else:
                    return render(request, 'login.html',
                                  {
                                      "username": username,
                                      "password": password,
                                      "message": "请联系管理员开通权限"
                                  })
            else:
                return render(request, 'login.html',
                              {
                                  "username": username,
                                  "password": password,
                                  "message": "用户名或密码错误，请检查后并重新输入"
                              })
        elif username == '':
            return render(request, 'login.html',
                          {
                              "username": '',
                              "password": '',
                              "message": "请输入用户名"
                          })
        elif password == '':
            return render(request, 'login.html',
                          {
                              "username": username,
                              "password": "",
                              "message": "请输入用户密码"
                          })
        else:
            return render(request, 'register.html',
                          {
                              "message": "用户未注册，请注册"
                          })


def user_logout(request):
    # 退出清理session
    request.session.clear()
    return redirect('/autotest/login/')
