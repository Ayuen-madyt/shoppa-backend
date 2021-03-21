from django.contrib import admin
from .models import Drink, Order

# Register your models here.
class OrderInline(admin.StackedInline): 
    model = Order

class ArticleAdmin(admin.ModelAdmin): 
    inlines = [
        OrderInline,
    ]

admin.site.register(Drink, ArticleAdmin) 
admin.site.register(Order)

 