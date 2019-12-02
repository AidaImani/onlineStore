from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug', 'category', 'price', 'stock', 'available', 'created','update']
    list_filter = ['category', 'created', 'update', 'available']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Product, ProductAdmin)
