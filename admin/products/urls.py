from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', views.ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', views.UserAPIView.as_view())
]