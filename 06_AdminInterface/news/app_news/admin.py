from django.contrib import admin
from .models import News, Status, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_news', 'status']

class StatusAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id_news', 'name', 'text_comment']

admin.site.register(News, NewsAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Comment, CommentAdmin)