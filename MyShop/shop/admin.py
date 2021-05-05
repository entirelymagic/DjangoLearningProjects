from django.contrib import admin
from .models import Category, Product


# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    list_filter = ('name', )
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'created', 'slug')
    list_filter = ('name', 'category', 'price', 'available', 'created')
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)
    ordering = ('name',)
