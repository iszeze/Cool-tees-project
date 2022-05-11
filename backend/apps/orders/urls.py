from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrderAdd.as_view(), name= 'order_list'),
]