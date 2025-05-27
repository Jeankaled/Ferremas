from django.urls import path
from .views import PedidoListCreateView, PedidoDetailView,Detalle_PedidoListCreateView, Detalle_PedidoDetailView, ClientePedidoList, ClientePedidoDetail

urlpatterns = [
    path('', PedidoListCreateView.as_view(), name='pedido-list'),
    path('<int:pk>/', PedidoDetailView.as_view(), name='pedido-detail'),
    path('detalle/', Detalle_PedidoListCreateView.as_view(), name='detalle-list'),
    path('detalle/<int:pk>/', Detalle_PedidoDetailView.as_view(), name='detalle-detail'),
    path('cliente/', ClientePedidoList.as_view(), name='cliente-list'),
    path('cliente/<int:pk>/', ClientePedidoDetail.as_view(), name='cliente-detail'),
]