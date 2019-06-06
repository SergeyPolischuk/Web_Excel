from django.contrib import admin
from .models import *
# from django.db.models.options import Options


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'customer_name', 'customer_phone', 'customer_email', 'description'[:15], 'date_created', 'date_deadline', 'status']

    class Meta:
        model = Order


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'date_created']

    class Meta:
        model = Status


admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)


# class OrderAdmin(admin.ModelAdmin):
#
#     list_display = [field.name for field in Order.]
#
#     class Meta:
#         model = Order
#
# admin.site.register(Order, OrderAdmin)