#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '22/07/2017'
__author__ = 'deling.ma'
"""
from django.conf.urls import url

from account import views

urlpatterns = [
    url(r'^reset_pwd/$', views.ResetPasswordView.as_view(), name="reset_pwd"),
    url(r'^register/$', views.RegisterView.as_view(), name="register"),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
]
