from django.contrib import admin
from .models import BlogEntry

@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'views_count', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'content')
