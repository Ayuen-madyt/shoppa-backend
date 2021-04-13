from django.urls import path
from .views import OrderItemSerializerView, OrdersSerializerView

urlpatterns = [
    path('orderitem/', OrderItemSerializerView.as_view()),
    path('orders/', OrdersSerializerView.as_view()),
]