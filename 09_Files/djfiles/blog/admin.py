from django.contrib import admin
from .models import UploadingFiles, BlogEntry

class AdminUploadingFiles(admin.TabularInline):
    model = UploadingFiles

class AdminBlogEntry(admin.ModelAdmin):
    inlines = [
        AdminUploadingFiles,
    ]

admin.site.register(BlogEntry, AdminBlogEntry)