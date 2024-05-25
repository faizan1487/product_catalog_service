from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name', 'description')

# Alternatively, you can register the model using the admin.site.register method:
# admin.site.register(Product, ProductAdmin)
