from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Created_date', 'Published_date')
    search_fields = ['Title', 'Text']

admin.site.register(Post, PostAdmin)
