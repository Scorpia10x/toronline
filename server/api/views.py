from rest_framework import viewsets
from .serializers import ProxySerializer
from .models import Proxy

class ProxyViewSet(viewsets.ModelViewSet):
    queryset = Proxy.objects.all().order_by('rate').reverse()
    serializer_class = ProxySerializer