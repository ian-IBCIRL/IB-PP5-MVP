from django.contrib import admin
from .models import Product, Category, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )


ordering = ('sku',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment management section for admin
    """
    list_display = ('name', 'body', 'product', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
