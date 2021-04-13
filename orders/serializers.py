from rest_framework import serializers
from .models import Orders, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['user', 'item', 'quantity', 'get_total_item_price']

class OrdersSerializer(serializers.ModelSerializer):
    # items_ordered = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Orders
        fields = ['user', 'items_ordered','date_added', 'delivered']
