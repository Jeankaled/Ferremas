from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import PedidoViewSet, PedidoClienteViewSet
from clientes.views import ClienteViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'detalles-pedidos', PedidoClienteViewSet, basename='pedido-detalle')
router.register(r'clientes', ClienteViewSet, basename='cliente')

clientes_router = routers.NestedDefaultRouter(router, r'clientes', lookup='cliente')
clientes_router.register(r'pedidos', PedidoClienteViewSet, basename='cliente-pedido')


urlpatterns = [
  path('', include(router.urls)),
  path('', include(clientes_router.urls)),
]