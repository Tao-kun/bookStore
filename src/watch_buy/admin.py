from django.contrib import admin

from watch_buy.models import Cart, Goods, GoodsPic, Order, OrderGood


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['studentID', 'GoodID', 'Qty']})
    ]
    list_display = ['studentID', 'GoodID']


class GoodsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('基本信息', {'fields': ['GoodISBN', 'GoodName', 'GoodPrice', 'GoodAuthor', 'GoodIntro']}),
        ('销售信息', {'fields': ['GoodRemain', 'GoodDiscount', 'IsForSale', 'IsNew']}),
        ('其他', {'fields': ['Intro_pic']})
    ]
    list_display = ['GoodName', 'GoodISBN', 'GoodRemain']


class GoodsPicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['GoodISBN', 'GoodPic']})
    ]


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderGoodAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cart, CartAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsPic, GoodsPicAdmin)
admin.site.register(Order)
admin.site.register(OrderGood)
