from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import InventarioViewSet, ProductoInventarioViewSet
from productos.views import ProductoViewSet

router = DefaultRouter()
router.register(r'inventario', InventarioViewSet, basename='inventario')

router.register(r'productos', ProductoViewSet, basename='producto')

productos_router = routers.NestedDefaultRouter(router, r'productos', lookup='producto')
productos_router.register(r'inventario', ProductoInventarioViewSet, basename='producto-inventario')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(productos_router.urls)),
]