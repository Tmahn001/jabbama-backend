from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryViewSet, ProductViewSet, UserDetailsView, Product_Category_ViewSet, OrderRetrieveUpdateView, OrderListCreateView, PaymentViewSet

router = routers.DefaultRouter()
router.register(r'category_product', CategoryViewSet)
router.register(r'product_item', ProductViewSet)
router.register(r'payments', PaymentViewSet)



urlpatterns=[
    path('api/', include(router.urls)),
    path('me/', UserDetailsView.as_view(), name='me'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateView.as_view(), name='order-retrieve-update'),
    path('categories/<str:category_id>/', Product_Category_ViewSet.as_view({'get': 'list'}), name='category-products')

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)