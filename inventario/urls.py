from django.urls import path
from .views import InventarioList, InventarioDetail, productoInventarioList, productoInventarioDetail

urlpatterns = [
    path('inventario/', InventarioList.as_view(), name='inventario-list'),
    path('inventario/<int:pk>/', InventarioDetail.as_view(), name='inventario-detail'),

    path('producto/', productoInventarioList.as_view(), name='producto-list'),
    path('producto/<int:pk>/', productoInventarioDetail.as_view(), name='producto-detail'),
]