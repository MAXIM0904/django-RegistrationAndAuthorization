from django.contrib import admin
from .models import News, Author_news, Status_news

@admin.register(News)
class News_Admin(admin.ModelAdmin):
    pass

@admin.register(Author_news)
class Author_news_Admin(admin.ModelAdmin):
    pass

@admin.register(Status_news)
class Status_news_Admin(admin.ModelAdmin):
    pass
