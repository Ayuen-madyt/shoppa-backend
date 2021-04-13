from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Drink,Order
    

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'cover_picture', 'category', 'brand', 'price', 'previous_price', 'discount']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['amount','area', 'customer', 'delivery' ,'drink', 'location', 'payment','phone', 'quantity']

