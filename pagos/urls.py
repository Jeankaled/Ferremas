from django.urls import path, include
from rest_framework.routers import DefaultRouter
from  rest_framework_nested import routers

from .views import PagoViewSet, PagoClienteViewSet
from clientes.views import ClienteViewSet

router = DefaultRouter()
router.register(r'pagos', PagoViewSet, basename='pago')
router.register(r'clientes', ClienteViewSet, basename='cliente')

clientes_router = routers.NestedDefaultRouter(router, r'clientes', lookup='cliente')
clientes_router.register(r'pagos', PagoClienteViewSet, basename='cliente-pago')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(clientes_router.urls)),
]