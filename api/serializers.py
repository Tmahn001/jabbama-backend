from rest_framework import serializers
from .models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    # Define a SerializerMethodField for the read-only field 'slug'
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'product_image', 'description', 'slug']

    # Define a method to compute the value of 'slug'
    def get_slug(self, obj):
        # Assuming that 'slug' is a field in your Category model
        return obj.slug



class WriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'on_discount', 'discount_price', 'category', 'stock', 'description', 'image']

class ReadProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'on_discount', 'discount_price', 'category', 'stock', 'description', 'image']
        read_only_fields = fields

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'