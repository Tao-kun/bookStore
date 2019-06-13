from django.contrib import admin

from after_sold.models import Comment


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', ('good', 'quality'), 'content']})
    ]
    list_display = ['c_time', 'user', 'good', 'quality', 'content']
    search_fields = ['content', 'user__name', 'good__GoodName', 'good__GoodISBN']


admin.site.register(Comment, CommentAdmin)
