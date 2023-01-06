from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name="home"),
    path('create',create,name='create'),
    path('blog',blog,name="blog"),
    path('blogcomment',blogcomment,name="blogcomment"),
    path('myblog',myblog,name="myblog"),
    path('contact',contact,name="contact"),
    path('<int:pk>',edit,name='edit'),
    path('delete/<int:pk>',delete,name='delete'),
    path('thanks',thanks,name='thanks'),
    path('register',register,name="register"),
    path('login',auth_views.LoginView.as_view(template_name='login.html'),name="login"),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name="logout"),
    path('password_reset',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name="password_reset"),
    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
    
]