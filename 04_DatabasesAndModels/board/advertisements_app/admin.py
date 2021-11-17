from django.contrib import admin
from .models import Advertisement, Author, Category


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AdvertisementAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class AdvertisementAdmin(admin.ModelAdmin):
    pass