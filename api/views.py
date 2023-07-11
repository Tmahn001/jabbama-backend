from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .models import Category, Product, Order
from .serializers import CategorySerializer, WriteProductSerializer, ReadProductSerializer, OrderSerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category")
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name",)
    ordering_fields = ("price", "stock")
    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadProductSerializer
        return WriteProductSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer