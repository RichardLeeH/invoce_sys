# coding=utf-8
from django.contrib import admin

from invoice.models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "figure_img", "info", "ctime")
    search_fields = ("invoice_code", "user__username")
    list_filter = ("ctime", )

    def figure_img(self, obj):
        return '<img src="%s" alt="icon img" width="500px" />' % obj.figure.url

    figure_img.short_description = "发票图"
    figure_img.allow_tags = True
    
    def info(self, obj):
        return obj.info_format()

    info.short_description = "发票信息"
    info.allow_tags = True


admin.site.register(Invoice, InvoiceAdmin)
