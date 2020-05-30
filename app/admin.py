from django.contrib import admin
from .models import Client, Order

# Register your models here.

class OrderInline(admin.TabularInline):
    model = Order

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline
    ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass