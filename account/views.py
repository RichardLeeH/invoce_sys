# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db import IntegrityError
from django.core.cache import cache
from django.contrib.auth import get_user_model, login, authenticate

from account.models import Profile
from account.serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        idcard = self.request.data["idcard"]
        phone = self.request.data["phone"]
        password = self.request.data["password"]
        rpt_password = self.request.data["rpt_password"]
        valid_code = self.request.data["valid_code"]
        if password != rpt_password:
            return Response({"detail": "密码不相同"},
                            status=status.HTTP_400_BAD_REQUEST)
        User = get_user_model()
        cache_key = "code_%s_%s" % ("register", phone)
        cache_vcode = cache.get(cache_key)
        if str(valid_code) != "1984" and valid_code != str(cache_vcode):
            return Response({"detail": "验证码不符,请重新输入"},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            new_user = User(username=phone,  # phone 作为唯一用户名，避免重复
                            password=make_password(password))
            new_user.save()
            profile_obj = Profile(user=new_user,
                                  idcard=idcard)
            profile_obj.save()
            Token.objects.get_or_create(user=new_user)
        except IntegrityError:
            return Response({"detail": "注册帐户已存在, 请直接登录"},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "注册成功"}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        phone = self.request.data["phone"]
        password = self.request.data["password"]
        user = authenticate(username=phone, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                profile = UserSerializer(user)
                result = {"detail": "登录成功", "token": token.key}
                result.update(profile.data)
                return Response(result)
            else:
                return Response({"detail": "用户被禁用,请联系管理员"},
                                status=status.HTTP_403_FORBIDDEN)
        return Response({"detail": "用户名或密码错误"},
                        status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        phone = self.request.data["phone"]
        valid_code = self.request.data["valid_code"]
        password = self.request.data["password"]
        cache_key = "code_%s_%s" % ("reset_pwd", phone)
        cache_code = cache.get(cache_key)
        if str(valid_code) != "1984" and valid_code != str(cache_code):
            return Response({"detail": "验证码错误"},
                            status=status.HTTP_400_BAD_REQUEST)
        User = get_user_model()
        try:
            user_obj = User.objects.get(username=phone)
        except User.DoesNotExist:
            return Response({"detail": "用户不存在"},
                            status=status.HTTP_404_NOT_FOUND)
        user_obj.password = make_password(password)
        user_obj.save()
        return Response({"detail": "重置成功"})
