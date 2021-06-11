from bot.models import Image, Merchant, Order, Product
from django.contrib import admin

# Register your models here.
admin.site.register(Merchant)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Order)