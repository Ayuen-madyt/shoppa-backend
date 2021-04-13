from django.shortcuts import render
from rest_framework import generics
from .models import Orders, OrderItem
from .serializers import OrderItemSerializer, OrdersSerializer

# Create your views here.
class OrdersSerializerView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrderItemSerializerView (generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    # automatically set ordered_by field to the current login user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     queryset = Orders.objects.all()
    #     serializer = OrdersSerializer(queryset, many=True)
    #     order, created = Orders.object.get_or_create(user=user, delivered=False)

    #     serializer = SnippetSerializer(snippets, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    
            

    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = SnippetSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse(serializer.errors, status=400)