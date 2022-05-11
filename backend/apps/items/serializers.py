from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null = True)
    class Meta:
        model = Item
        fields = '__all__'