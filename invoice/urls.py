#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '22/07/2017'
__author__ = 'deling.ma'
"""
from rest_framework import routers

from invoice import views

router = routers.DefaultRouter()
router.register(r'invoice', views.InvoiceViewSet)

urlpatterns = router.urls
