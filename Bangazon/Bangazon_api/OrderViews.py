from Bangazon_api.models import *
from Bangazon_api.serializers import *
from rest_framework import generics

class OrderList(generics.ListCreateAPIView):
    """
    List all Orders, or create a new Order.
    """
    queryset = Bangazon_api.objects.all()
    serializer_class = OrderSerializer


class OrderDetails(generics.RetreiveUpdateDestroyAPIView):
    """
    List Order details.
    """
    queryset = Bangazon_api.objects.all()
    serializer_class = OrderSerializer
