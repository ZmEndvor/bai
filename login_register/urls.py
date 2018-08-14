from django.urls import path
from . import views

app_name = 'lisd'

urlpatterns = [
    # 登录登出
    path('login/', views.login_html, name='login'),
    path('signin_login/', views.signin_login, name='signin_login'),
    path('login_out/', views.login_out, name='login_out'),
    # 注册
    path('register/', views.register, name='register'),
    path('register_submit/', views.register_submit, name='register_submit'),
    # 修改密码
    path('change/', views.change_password, name='change_name'),
]
