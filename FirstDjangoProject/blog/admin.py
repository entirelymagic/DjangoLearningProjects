from django.contrib import admin
from .models import Post, Comment, Author


# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'active', 'post')
    list_filter = ('email', 'created', 'name', 'email')
    search_fields = ('name', 'body', 'email',)


