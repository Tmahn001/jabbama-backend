from rest_framework import serializers
from .models import Category, Product, Order, OrderItem, Payment

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
        fields = ['name', 'price', 'on_discount', 'discount_price', 'category', 'stock', 'description', 'image', 'color']

class ReadProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'on_discount', 'discount_price', 'category', 'stock', 'description', 'image', 'color']
        read_only_fields = fields

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, write_only=True)  # Use write_only=True for input data

    class Meta:
        model = Order
        fields = ['id', 'total_price', 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items', [])
        order = Order.objects.create(customer=self.context['request'].user, **validated_data)
        for item_data in order_items_data:
            print("Item Data:", item_data)
            product_name = item_data['product']
            print("Product ID:", product_name)
            quantity = item_data['quantity']
            product = Product.objects.get(name=product_name)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)


        self.update_total_price(order)
        return order

    def update_total_price(self, order):
        total_price = sum(item.product.discount_price * item.quantity for item in order.orderitem_set.all())
        order.total_price = total_price + 1500
        order.save()


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order', 'amount', 'transaction_id', 'status']
    
    def create(self, validated_data):
        user = self.context['request'].user  # Get the logged-in user
        validated_data['user'] = user  # Associate the user with the payment
        payment = Payment.objects.create(**validated_data)
        return payment