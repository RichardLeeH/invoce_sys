# coding=utf-8
from django.contrib import admin

from invoice.models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "invoice_code", "figure_img", "invoice_no", "ctime")
    search_fields = ("invoice_code", "user_id")
    list_filter = ("ctime", )

    def figure_img(self, obj):
        return '<img src="%s" alt="icon img" width="400px" />' % obj.figure.url

    figure_img.short_description = u"发票图"
    figure_img.allow_tags = True

admin.site.register(Invoice, InvoiceAdmin)
