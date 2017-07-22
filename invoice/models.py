# coding=utf-8
from django.conf import settings
from django.db import models


class Invoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    invoice_code = models.CharField("发票代码", max_length=36)
    invoice_no = models.CharField("发票号码", max_length=36)
    figure = models.ImageField("发票图", upload_to="invoice/figure", blank=True)
    ctime = models.DateTimeField("创建时间", auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "invoice"
        verbose_name = "发票信息"
        verbose_name_plural = "发票信息"

    def __str__(self):
        return "uid:%s, %s" % (self.user_id, self.invoice_code)
