from rest_framework import serializers
from .models import ProductFeatured

class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeatured
        fields = '__all__'