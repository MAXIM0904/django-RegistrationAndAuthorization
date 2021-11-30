from django.contrib import admin
from .models import News, Comment

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_news', 'status']
    list_filter = ('status',)
    search_fields = ('name',)
    inlines = [CommentInLine]
    list_editable = ('status',)

    actions = ['mark_as_actions', 'mark_as_inactive']

    def mark_as_actions(self, request, queryset):
        queryset.update(status="y")

    def mark_as_inactive(self, request, queryset):
        queryset.update(status="n")

    mark_as_inactive.short_description = 'Перевести в статус неактивно'
    mark_as_actions.short_description = 'Перевести в статус активно'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id_news', 'author', 'text_comment']
    list_filter = ('author',)
    search_fields = ('author', 'text_comment',)


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)