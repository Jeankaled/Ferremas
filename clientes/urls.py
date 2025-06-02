from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet



router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
# The basename is used to create the URL names for the viewset



urlpatterns = [
    path('', include(router.urls)),
]