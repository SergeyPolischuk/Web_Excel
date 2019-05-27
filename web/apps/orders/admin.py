from django.contrib import admin
from .models import *
# from django.db.models.options import Options


# Register your models here.
admin.site.register(Order)
admin.site.register(Status)


# class OrderAdmin(admin.ModelAdmin):
#
#     list_display = [field.name for field in Order.]
#
#     class Meta:
#         model = Order
#
# admin.site.register(Order, OrderAdmin)