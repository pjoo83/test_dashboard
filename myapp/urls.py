from django.urls import path
from .views import login_view, register_view

urlpatterns = [
    # 登陆注册
    path("login/", login_view.user_login, name='user_login'),
    path("register/", register_view.user_register, name='user_register')
]
