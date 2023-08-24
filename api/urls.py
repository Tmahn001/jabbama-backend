from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryViewSet, ProductViewSet, UserDetailsView, Product_Category_ViewSet

router = routers.DefaultRouter()
router.register(r'category_product', CategoryViewSet)
router.register(r'product_item', ProductViewSet)



urlpatterns=[
    path('api/', include(router.urls)),
    path('me/', UserDetailsView.as_view(), name='me'),
    path('categories/<str:category_id>/', Product_Category_ViewSet.as_view({'get': 'list'}), name='category-products')

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)