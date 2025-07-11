# carrito/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views       import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response    import Response
from transbank.webpay.webpay_plus.transaction import Transaction
import time
from .models import Cart, CartItem
from .serializers import CartSerializer
from productos.models import Producto

class CartViewSet(viewsets.ViewSet):
 
    permission_classes = [AllowAny]  
    
    def _get_or_create_cart(self, request):
        cart_id = request.session.get("cart_id")
        if cart_id:
            cart = Cart.objects.filter(pk=cart_id).first()
            if cart:
                return cart
        cart = Cart.objects.create()
        request.session["cart_id"] = cart.id
        return cart

    def list(self, request):
        cart = self._get_or_create_cart(request)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def add(self, request):
     
        cart = self._get_or_create_cart(request)
        producto_id = request.data.get("producto_id")
        cantidad     = int(request.data.get("cantidad", 1))

        try:
            producto = Producto.objects.get(pk=producto_id)
        except Producto.DoesNotExist:
            return Response({"detail": "Producto no encontrado"}, status=404)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            producto=producto,
            defaults={"cantidad": cantidad}
        )
        if not created:
            item.cantidad += cantidad
            item.save()

        return Response(CartSerializer(cart).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def remove(self, request):
        """
        POST /cart/remove/
        Body: { producto_id: <id> }
        """
        cart = self._get_or_create_cart(request)
        producto_id = request.data.get("producto_id")
        CartItem.objects.filter(cart=cart, producto_id=producto_id).delete()
        return Response(CartSerializer(cart).data, status=status.HTTP_200_OK)


class CheckoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        cart_id = request.session.get("cart_id")
        if not cart_id:
            return Response({"detail": "No hay carrito en sesión"}, status=400)
        cart = Cart.objects.filter(pk=cart_id).first()
        if not cart:
            return Response({"detail": "Carrito no encontrado"}, status=404)

        total = sum(item.producto.precio_actual * item.cantidad for item in cart.items.all())
       
        buy_order  = f"{cart.id}-{int(time.time())}"
        session_id = str(cart.id)
        return_url = request.build_absolute_uri("/cart/confirm/")

        response = Transaction.create(
            buy_order   = buy_order,
            session_id  = session_id,
            amount      = int(total),
            return_url  = return_url,
        )

        return Response({
            "url":   response.url,
            "token": response.token
        })
    
    
    
class ConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.data.get("token_ws")
        response = Transaction.commit(token)
        if response.response_code == 0:
            return Response({"detalle": "Pago exitoso"})
        return Response({"detalle": "Error en pago"}, status=400)

    
