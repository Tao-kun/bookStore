from django.contrib import admin

# Register your models here.

from watch_buy.models import *
from login_manage.models import User

admin.site.register(Goods)
admin.site.register(User)
admin.site.register(Cart)