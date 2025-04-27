from django.contrib import admin
from .models import Customer, Product, Order, Shipping, Payment, ProductOrder

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_first_name', 'get_last_name', 'province', 'post_code', 'tel')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'province', 'post_code', 'tel')
    list_filter = ('province',)
    ordering = ('id',)

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    ordering = ('id',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'status', 'shipping', 'payment')
    search_fields = ('customer__username', 'status', 'total_price')
    list_filter = ('status', 'shipping', 'payment')
    ordering = ('id',)

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('id', 'method')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'method')

@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order', 'quantity', 'total_price')
    search_fields = ('product__name', 'order__id')
    list_filter = ('product',)
    ordering = ('id',)
