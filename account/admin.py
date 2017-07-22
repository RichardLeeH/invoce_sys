# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from account.models import Profile

admin.site.site_header = 'invoce'


class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'uid', 'user', 'created')
    fields = ('user',)
    ordering = ('-created',)

    def uid(self, obj):
        return obj.user.id
    uid.short_description = u'用户ID'

admin.site.unregister(Token)
admin.site.register(Token, TokenAdmin)


class ProfileInline(admin.StackedInline):
    model = Profile


class UserCustomAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff')
    inlines = (ProfileInline, )
    ordering = ('-id', )

admin.site.unregister(User)
admin.site.register(User, UserCustomAdmin)
