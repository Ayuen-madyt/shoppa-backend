from django.shortcuts import render
from rest_framework import generics, permissions
from .models import ProductFeatured
from .serializers import FeaturedSerializer

# admin should have permissions to this view only
class FeaturedSerializerListAdminView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,) 
    queryset = ProductFeatured.objects.all()
    serializer_class = FeaturedSerializer

# admin should have permissions to this view only
class FeaturedSerializerDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,) 
    queryset = ProductFeatured.objects.all()
    serializer_class = FeaturedSerializer

# client end point view
class FeaturedSerializerListView(generics.ListAPIView):
    queryset = ProductFeatured.objects.all()
    serializer_class = FeaturedSerializer