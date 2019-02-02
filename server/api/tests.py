from rest_framework.test import APITestCase

from .models import Proxy


class ProxyTests(APITestCase):

    def prepare_proxies(self):

        self.proxies= [
            { 'name' : 'ws',   'rate' : 8 },
            { 'name' : 'pet',  'rate' : 9 },
            { 'name' : 'link', 'rate' : 0 },
            { 'name' : 'to',   'rate' : 1 },
        ]

        for proxy in self.proxies:
            test_proxy = Proxy(name = proxy['name'], rate = proxy['rate'])
            test_proxy.save()

        return self.proxies

    def setUp(self):
        self.prepare_proxies()

    def test_proxies_order(self):
        response = self.client.get('/proxy/', format='json')
        self.assertEqual(response.status_code, 200)

        proxies = response.data['results']
        self.assertListEqual( [proxy['name'] for proxy in proxies],
                              ['pet', 'ws', 'to', 'link'] )

    def test_nonexistent_proxy(self):
        response = self.client.get('/proxy/nonexistent/', format='json')
        self.assertNotEqual(response.status_code, 200)