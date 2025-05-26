from django.urls import path
from .views import PagoList, PagoDetail, ClientePagoList, ClientePagoDetail, ClientePagoList, ClientePagoDetail

urlpatterns = [
    path('pago/', PagoList.as_view(), name='pago-list'),
    path('pago/<int:pk>/', PagoDetail.as_view(), name='pago-detail'),

    path('cliente/', ClientePagoList.as_view(), name='cliente-list'),
    path('cliente/<int:pk>/', ClientePagoDetail.as_view(), name='cliente-detail'),
]