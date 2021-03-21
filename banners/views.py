from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import BannerSerializer
from .models import Banner

# Create your views here.

# admin endpoint
class BannerSerializerListAdminView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,) 
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

# admin enpoint
class BannerSerializerDetailAdminView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,) 
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

# client readonly api
class BannerSerializerView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
