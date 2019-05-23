from django.contrib import admin

from watch_buy.models import Cart, Goods, GoodsPic, Order, OrderGood


class GoodsPicInline(admin.TabularInline):
    model = GoodsPic
    extra = 0


class OrderGoodInline(admin.TabularInline):
    model = OrderGood
    extra = 0


# Register your models here.

class CartAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['studentID', 'GoodID', 'Qty']})
    ]
    list_display = ['studentID', 'user_name', 'good_isbn', 'good_name']

    def user_name(self, obj):
        return obj.studentID.name

    def good_isbn(self, obj):
        return obj.GoodID.GoodISBN

    def good_name(self, obj):
        return obj.GoodID.GoodName

    user_name.short_description = '姓名'
    good_isbn.short_description = 'ISBN'
    good_name.short_description = '书籍名称'


class GoodsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('基本信息', {'fields': ['GoodISBN', 'GoodName', 'GoodPrice', 'GoodAuthor', 'GoodIntro']}),
        ('销售信息', {'fields': ['GoodRemain', 'GoodDiscount', 'IsForSale', 'IsNew']}),
        ('其他', {'fields': ['Intro_pic']})
    ]
    list_display = ['GoodName', 'GoodISBN', 'GoodRemain']
    inlines = [GoodsPicInline]


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('订单信息', {'fields': ['orderdate', 'shipdate', 'user', 'IsShipped', 'IsCancle', 'IsHandled', 'IsCancled']}),
        ('收货人信息', {'fields': ['username', 'telephone', 'address', 'zipcode', 'qq']})
    ]
    list_display = ['username', 'address', 'orderdate', 'show_is_shipped']
    inlines = [OrderGoodInline]

    def show_is_shipped(self, obj):
        if obj.IsShipped == 0:
            return '否'
        return '是'

    show_is_shipped.short_description = '是否发货'


admin.site.register(Cart, CartAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Order, OrderAdmin)
