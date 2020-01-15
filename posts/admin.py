# imports
from django.contrib import admin
from .models import Post

# Register your models here.

# to show full details of each post on admin panel
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish', 'author')
	search_fields = ('title', 'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	data_hierarchy = 'publish'
	ordering = ('status', 'publish')