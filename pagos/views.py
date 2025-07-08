from django.shortcuts import render
from requests import Response
from rest_framework import viewsets
from .models import Pago
from .serializers import PagoSerializer
from django.conf import settings
from django.http import HttpResponse, JsonResponse


from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes


# Create your views here.

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    
    def create(self, request, *args, **kwargs):
        options = WebpayOptions(
            integration_type=IntegrationType.TEST,
            api_key=IntegrationApiKeys.WEBPAY_PLUS_API_KEY,
            commerce_code=IntegrationCommerceCodes.WEBPAY_PLUS_COMMERCE_CODE
        )
        tx = Transaction(options)
        response = tx.create(
            buy_order=request.data.get('buy_order'),
            session_id=request.data.get('session_id'),
            amount=request.data.get('monto'),
            return_url=request.data.get('')
        )
        token = response[token]
        
        datos = request.data.copy()
        datos['token'] = token
        serializer = self.serializer_class(data=datos)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
class PagoClienteViewSet(viewsets.ModelViewSet):
    serializer_class = PagoSerializer

    def get_queryset(self):
        cliente_id = self.kwargs.get('cliente_id')
        return Pago.objects.filter(cliente_id=cliente_id)

    def perform_create(self, serializer):
        cliente_id = self.kwargs.get('cliente_id')
        serializer.save(cliente_id=cliente_id)
        
