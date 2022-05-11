from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .serializers import ItemSerializer
from django.http import JsonResponse
from .models import Item 


class ItemList(generics.ListAPIView):
    queryset =Item.objects.order_by('created_at').reverse().filter(status = 'active')
    serializer_class = ItemSerializer