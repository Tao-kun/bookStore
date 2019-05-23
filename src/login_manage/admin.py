from django.contrib import admin

from login_manage.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('账户信息', {'fields': ['studentID', 'email', 'name', 'password', 'money', 'is_banned']}),
        ('个人信息', {'fields': ['city', 'detail_address', 'zip_code', 'qq']}),
    ]
    list_display = ['studentID', 'name', 'email', 'is_banned']


admin.site.register(User, UserAdmin)
