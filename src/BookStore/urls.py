"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from after_sold import views as after_sold_views
from login_manage import views as login_manage_views
from watch_buy import views as watch_buy_views
from after_sold.views import *

admin.site.site_header = '系统管理'
admin.site.site_title = '系统管理'

# TODO: 部署时添加路由/media/
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', login_manage_views.index),
    url(r'^login/', login_manage_views.login),
    url(r'^register/', login_manage_views.register),
    url(r'^logout/', login_manage_views.logout),
    url(r'^test/', login_manage_views.test),
    url(r'^is_valid/', login_manage_views.is_valid),
    url(r'^add_to_db/', login_manage_views.add_to_db),
    url(r'^forget_password/', login_manage_views.sendemail),
    url(r'^catalog_grid/', watch_buy_views.catalog_grid),
    url(r'^checkout/', watch_buy_views.checkout),
    url(r'^shopping_cart/', watch_buy_views.shopping_cart),
    url(r'^add_to_cart/', watch_buy_views.add_to_cart),
    url(r'^user_info/', login_manage_views.user_info),
    url(r'^update_user/', login_manage_views.update_user),
    url(r'^product_page/', watch_buy_views.good_detail),
    url(r'^add_order/', watch_buy_views.add_order),
    url(r'^past_comment/', post_comments),
    url(r'^show_comments/',watch_buy_views.show_comments),
    url(r'^see_order/', after_sold_views.see_order),
    url(r'^order_detail/', after_sold_views.order_detail),
    url(r'^delete_item/', watch_buy_views.delete_item),
    url(r'^changeqty/', watch_buy_views.changeqty),
    url(r'^delete_all/', watch_buy_views.delete_all),
    url(r'^confirm_order/', after_sold_views.confirm_order),
    url(r'^confirm_receive/', after_sold_views.confirm_receive),
    url(r'^cancel_order/', after_sold_views.calcel_order),
    url(r'^apply_return/', after_sold_views.apply_return),
    url(r'^comment_order/', after_sold_views.comment_order),
    url(r'^cancel_return/', after_sold_views.cancel_return),
    url(r'^$', login_manage_views.index)
]
