
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaProductoViewSet, PrecioProductoViewSet, ProductoViewSet

app_name = 'productos'

# Vista de plantilla
urlpatterns = [
  
]

# API
router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'categorias',   CategoriaProductoViewSet,basename='categoria')
router.register(r'precios',      PrecioProductoViewSet,   basename='precio')

urlpatterns += [
    path('', include(router.urls)),
]
