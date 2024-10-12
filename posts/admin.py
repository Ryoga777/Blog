from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date"]
    list_filter = ["date"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostModelAdmin)