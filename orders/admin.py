from django.contrib import admin
from .models import OrderItem, Orders

# Register your models here.
admin.site.register(OrderItem)
admin.site.register(Orders)
