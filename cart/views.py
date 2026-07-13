from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Cart
from .serializers import CartSerializer


class CartListCreateView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer