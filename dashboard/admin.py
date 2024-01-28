from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')


admin.site.register(Product, ProductAdmin)

class DetailAdmin (admin.ModelAdmin):
    list_display = ('product','feature')

admin.site.register(details,DetailAdmin)

class AddToCartAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'added_at') 

admin.site.register(AddToCart, AddToCartAdmin)
