from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView
from .models import Cart 

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        depth = 1

class CartAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart 
        fields = '__all__'
        