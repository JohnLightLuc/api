from django.contrib import admin
from django.contrib.admin import register
from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'article_heading', 'article_body')