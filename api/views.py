from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from .models import Category, Product, Order
from .serializers import CategorySerializer, WriteProductSerializer, ReadProductSerializer, OrderSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from accounts.models import CustomUser

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

class Product_Category_ViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("name",)
    ordering_fields = ("price", "stock")

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        try:
            category = Category.objects.get(slug=category_id)
            products = Product.objects.filter(category=category)
            return products
        except Category.DoesNotExist:
            return Product.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        category_id = self.kwargs['category_id']
        category_data = Category.objects.filter(slug=category_id).values('id', 'name', 'product_image', 'description', 'slug').first()
        
        response_data = {
            "count": 1,  # Only one category
            "next": None,
            "previous": None,
            "category": category_data,
            "results": serializer.data
                            
        }
        
        return Response(response_data)
    
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

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user_data = {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            
            
        }

        return Response(user_data)

