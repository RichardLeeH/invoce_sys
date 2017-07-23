# coding=utf-8
from django.conf import settings
from django.db import models


class Invoice(models.Model):
    user               = models.ForeignKey(settings.AUTH_USER_MODEL)

    invoice_code       = models.CharField("发票代码", max_length=36)
    invoice_no         = models.CharField("发票号码", max_length=36)

    invoice_ctime      = models.DateTimeField("开票日期")

    buyer              = models.CharField("购买方名称", max_length=36)
    id_no              = models.CharField("身份证号码/组织机构代码", max_length=36)
    vehicletype        = models.CharField("车辆类型", max_length=36)
    make_type          = models.CharField("厂牌型号", max_length=100)
    origin             = models.CharField("产地", max_length=36)
    certification_no   = models.CharField("合格账号", max_length=36)
    engine_no          = models.CharField("发动机号", max_length=36)
    vin_no             = models.CharField("车架号", max_length=36)
    total_price_low    = models.FloatField("价税合计小写")
    total_price_upper  = models.CharField("价税合计大写", max_length=50)
    taxpayer_no        = models.CharField("纳税人识别码", max_length=50)
    retail_sales_units = models.CharField("销货单位", max_length=100)

    figure             = models.ImageField("发票图", upload_to="invoice/figure", blank=True)
    ctime              = models.DateTimeField("创建时间", auto_now_add=True)
    utime              = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "invoice"
        verbose_name = "发票信息"
        verbose_name_plural = "发票信息"

    def __str__(self):
        return "uid:%s, %s" % (self.user_id, self.invoice_code)
