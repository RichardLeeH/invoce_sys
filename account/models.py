# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    idcard = models.CharField("员工编号", max_length=16, blank=True, unique=True)
    age = models.IntegerField("年龄", default=0)
    nickname = models.CharField("姓名", max_length=36, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_profile"
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"
    
    @property
    def phone(self):
        return self.user.username

    def __str__(self):
        return "uid:%s, %s" % (self.user_id, self.idcard)
