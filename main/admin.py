from django.contrib import admin
from .models import Article
from django.db import models

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
		('Source', {'fields': ['source', 'author', 'title', 'publishedAt']}),
		('URL', {'fields': ['url', 'urlToImg']}),
		('Article Description', {'fields': ['description', 'content']}),
	]

admin.site.register(Article, ArticleAdmin)