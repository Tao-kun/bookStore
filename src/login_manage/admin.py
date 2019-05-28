from django import forms
from django.contrib import admin

from login_manage.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('账户信息', {'fields': ['studentID', 'email', 'name', 'password', 'money']}),
        ('个人信息', {'fields': ['city', 'detail_address', 'zip_code', 'qq']}),
    ]
    list_display = ['studentID', 'name', 'email', 'user_ban_status']
    actions = ['ban_user', 'permit_user']
    list_filter = [
        ('is_banned', admin.BooleanFieldListFilter)
    ]
    form = UserForm

    def ban_user(self, request, queryset):
        rows_updated = queryset.update(is_banned=1)
        self.message_user(request, "{}个用户被成功封禁".format(rows_updated))

    def permit_user(self, request, queryset):
        rows_updated = queryset.update(is_banned=0)
        self.message_user(request, "{}个用户被成功解禁".format(rows_updated))

    def user_ban_status(self, obj):
        if obj.is_banned == 0:
            return '否'
        return '是'

    ban_user.short_description = '封禁所选的用户'
    permit_user.short_description = '解禁所选的用户'
    user_ban_status.short_description = '是否被封禁'


admin.site.register(User, UserAdmin)
