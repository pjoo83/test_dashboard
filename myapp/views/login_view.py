from django import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import render


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
                    # 权限装饰器
                    login(request,user)