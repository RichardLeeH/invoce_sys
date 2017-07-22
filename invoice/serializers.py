#!/usr/bin/env python
# coding=utf-8
"""

__created__ = '22/07/2017'
__author__ = 'deling.ma'
"""
from rest_framework import serializers

from invoice.models import Invoice


class InvoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ("id", "invoice_code", "invoice_no")
