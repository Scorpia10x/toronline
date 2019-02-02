from factory import DjangoModelFactory
from .models import Proxy

class ProxyFactory(DjangoModelFactory):
    class Meta:
        model = Proxy

    name = ''
    rate = 0
    replace_original_domain = False