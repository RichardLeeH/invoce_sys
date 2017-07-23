# coding=utf-8
from django.conf import settings
from django.db import models
from django.utils import timezone


class Invoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    invoice_code = models.CharField("发票代码", max_length=36)
    invoice_no = models.CharField("发票号码", max_length=36)
    invoice_ctime = models.DateTimeField("开票日期", default=timezone.now)
    buyer = models.CharField("购买方名称", max_length=36, blank=True)
    id_no = models.CharField("身份证号码/组织机构代码", max_length=36)
    vehicletype = models.CharField("车辆类型", max_length=36, blank=True)
    make_type = models.CharField("厂牌型号", max_length=100, blank=True)
    origin = models.CharField("产地", max_length=36, blank=True)
    certification_no = models.CharField("合格账号", max_length=36, blank=True)
    engine_no = models.CharField("发动机号", max_length=36, blank=True)
    vin_no = models.CharField("车架号", max_length=36, blank=True)
    total_price_low = models.FloatField("价税合计小写", default=0)
    total_price_upper = models.CharField("价税合计大写", max_length=50, blank=True)
    taxpayer_no = models.CharField("纳税人识别码", max_length=50, blank=True)
    retail_sales_units = models.CharField("销货单位", max_length=100, blank=True)
    
    figure = models.ImageField("发票图", upload_to="invoice/figure", blank=True)
    ctime = models.DateTimeField("创建时间", auto_now_add=True)
    utime = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "invoice"
        verbose_name = "发票信息"
        verbose_name_plural = "发票信息"
    
    def info_format(self):
        result = """
        发票代码: {invoice_code} <br/>
        发票号码: {invoice_no} <br/>
        购买方名称: {buyer} <br/>
        身份证|机构代码: {id_no} <br/>
        车辆类型: {vehicletype} <br/>
        厂牌型号: {make_type} <br/>
        产地: {origin} <br/>
        合格账号: {certification_no} <br/>
        发动机号: {engine_no} <br/>
        车架号: {vin_no} <br/>
        价税合计小写: {total_price_low} <br/>
        价税合计大写: {total_price_upper} <br/>
        纳税人识别码: {taxpayer_no} <br/>
        销货单位: {retail_sales_units} <br/>
        """.format(**self.__dict__)
        return result
    
    def __str__(self):
        return "uid:%s, %s" % (self.user_id, self.invoice_code)
