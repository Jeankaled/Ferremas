from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CheckoutView, ConfirmView



app_name = "cart"


router = DefaultRouter()
router.register(r'', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('checkout/', CheckoutView.as_view(), name='cart-checkout'),
    path('confirm/',  ConfirmView.as_view(),  name='cart-confirm'),
]
