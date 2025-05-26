from django.urls import path
from .views import ProductoList, ProductoDetail, CategoriaProductoList, CategoriaProductoDetail, PrecioProductoList, PrecioProductoDetail

urlpatterns = [
    path('', ProductoList.as_view(), name='producto-list'),
    path('<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),

    path('categoria/', CategoriaProductoList.as_view(), name='categoria-list'),
    path('categoria/<int:pk>/', CategoriaProductoDetail.as_view(), name='categoria-detail'),

    path('precio/', PrecioProductoList.as_view(), name='precio-list'),
    path('precio/<int:pk>/', PrecioProductoDetail.as_view(), name='precio-detail'),
]