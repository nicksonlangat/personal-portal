from blogs.models import Category, Post, Tag
from django.contrib import admin

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)