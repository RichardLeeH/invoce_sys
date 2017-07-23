from __future__ import absolute_import
import xadmin
from django.contrib.auth.models import User
from xadmin import views
from .models import Invoice


@xadmin.sites.register(views.website.IndexView)
class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "Test Widget",
             "content": "<h3> Welcome to Invoice! </h3>"},
            {"type": "chart", "model": "app.accessrecord", "chart": "user_count",
             "params": {"_p_date__gte": "2017-07-29", "p": 1, "_p_date__lt": "2017-07-29"}},
            {"type": "list", "model": "app.host", "params": {"o": "-guarantee_date"}},
        ],
        [
            {"type": "qbutton", "title": "Quick Start",
             "btns": [{"model": Invoice}, ]},
            {"type": "addform", "model": Invoice},
        ]
    ]


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    global_search_models = [Invoice, User]
    global_models_icon = {
        Invoice: "fa fa-laptop", User: "fa fa-cloud"
    }
    menu_style = 'default'  # 'accordion'


@xadmin.sites.register(Invoice)
class InvoiceAdmin(object):
    list_display = ("id", "figure_img", "info", "ctime")
    search_fields = ("invoice_code", "user__username")
    list_filter = ("ctime",)
    
    def figure_img(self, obj):
        return '<img src="%s" alt="icon img" width="500px" />' % obj.figure.url
    
    figure_img.short_description = "发票图"
    figure_img.allow_tags = True
    
    def info(self, obj):
        return obj.info_format()
    
    info.short_description = "发票信息"
    info.allow_tags = True

