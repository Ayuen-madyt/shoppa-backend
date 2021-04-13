from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import DrinkSerializer, OrderSerializer
from .models import Drink, Order
from rest_framework import filters

# admin should have permissions to this view only
class DrinkSerializerListAdminView(generics.ListCreateAPIView): 
    permission_classes = (permissions.IsAdminUser,) 
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

# admin should have permissions to this view only
class DrinkSerializerDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,) 
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

# client list api readonly end point
class DrinkSerializerListView(generics.ListAPIView): 
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

# client Detail api readonly end point
class DrinkSerializerDetailView(generics.RetrieveAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

# any customer is allowed to use this view for orders but they must be authenticated
# admin can use also use this view to analyze orders by customers
class OrderSerializerView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) 
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self):
        obj = super().get_object()
        obj.order_date = timezone.now()
        obj.save()
        return obj

    # automatically set ordered_by field to the current login user
    # def perform_create(self, serializer):
    #     serializer.save(customer=self.request.user)
        
   

# FILTERING 
# Search filter all drinks
class FilterListView(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category']

# filtering for wines and spirits only
class WinesAndSpiritsView(generics.ListAPIView):
    queryset = Drink.objects.filter(category="Wines and Spirits")
    serializer_class = DrinkSerializer

# filtering for Energy drinks only
class EnergyDrinksView(generics.ListAPIView):
    queryset = Drink.objects.filter(category="Energy Drinks")
    serializer_class = DrinkSerializer

# filtering for Soft drinks only
class SoftDrinksView(generics.ListAPIView):
    queryset = Drink.objects.filter(category="Soft Drinks")
    serializer_class = DrinkSerializer

# filtering for water only
class WaterView(generics.ListAPIView):
    queryset = Drink.objects.filter(category="Water")
    serializer_class = DrinkSerializer