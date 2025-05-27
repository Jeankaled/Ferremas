from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CategoriaProductoViewSet, PrecioProductoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='producto')  
router.register(r'categorias', CategoriaProductoViewSet, basename='categoria_producto')
router.register(r'precios', PrecioProductoViewSet, basename='precio_producto')

urlpatterns = [
    path('', include(router.urls)),
]