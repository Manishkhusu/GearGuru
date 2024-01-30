from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')


admin.site.register(Product, ProductAdmin)

class DetailAdmin (admin.ModelAdmin):
    list_display = ('product','feature')

admin.site.register(Detail,DetailAdmin)

class AddToCartAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'added_at') 

admin.site.register(AddToCart, AddToCartAdmin)


admin.site.register(PurchasedProduct)
# class BuynowAdmin(admin.ModelAdmin):
#     list_display = ('product', 'quantity', 'total_price', 'buyer_name', 'buyer_email', 'shipping_address', 'order_date')

# admin.site.register(Buynow, BuynowAdmin)
