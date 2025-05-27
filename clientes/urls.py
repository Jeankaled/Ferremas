from django.urls import path
from .views import ClienteList, ClienteDetail

urlpatterns = [
    path('cliente/', ClienteList.as_view(), name='cliente-list'),
    path('cliente/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),
]