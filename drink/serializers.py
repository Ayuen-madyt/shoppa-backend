from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Drink,Order
    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['ordered_by','drink', 'order_date', 'phone_number' ,'location', 'area', 'delivery_method']

class DrinkSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    class Meta:
        model = Drink
        fields = ['id', 'name', 'cover_picture', 'category', 'brand', 'price', 'previous_price', 'discount', 'orders']

