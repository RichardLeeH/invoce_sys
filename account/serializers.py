#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '22/07/2017'
__author__ = 'deling.ma'
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source="profile.nickname")
    phone = serializers.CharField(source="profile.phone")
    idcard = serializers.CharField(source="profile.idcard", read_only=True)

    class Meta:
        model = get_user_model()
        fields = ("date_joined", "id", "phone", "nickname")
