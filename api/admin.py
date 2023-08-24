from django.contrib import admin
from .models import Category, Product, Order, OrderItem

# Model admin classes
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'on_discount', 'stock')
    list_filter = ('category', 'on_discount')
    search_fields = ('name', 'category__name')
    list_editable = ('price', 'on_discount', 'stock')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('customer__username', 'customer__email')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    list_filter = ('order__created_at',)
    search_fields = ('order__customer__username', 'product__name')

# Register your model admin classes

