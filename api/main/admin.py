from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)