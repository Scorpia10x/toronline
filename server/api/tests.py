from rest_framework.test import APITestCase

from .factories import ProxyFactory


class ProxyTests(APITestCase):

    def prepare_proxies(self):

        self.proxies = [
            {'name': 'ws',         'rate': 8},
            {'name': 'pet',        'rate': 9},
            {'name': 'link',       'rate': 0},
            {'name': 'to',         'rate': 1},
            {'name': 'darknet.to', 'rate': 10, 'replace_original_domain': True}
        ]

        for proxy in self.proxies:
            ProxyFactory.create(name=proxy['name'], rate=proxy['rate'])

        return self.proxies

    def setUp(self):
        self.prepare_proxies()

    def test_proxies_order(self):
        response = self.client.get('/proxy/', format='json')
        self.assertEqual(response.status_code, 200)

        proxies = response.data['results']
        proxy_names = [proxy['name'] for proxy in proxies]
        self.assertListEqual(proxy_names, ['darknet.to', 'pet', 'ws', 'to', 'link'])

    def test_nonexistent_proxy(self):
        response = self.client.get('/proxy/nonexistent/', format='json')
        self.assertNotEqual(response.status_code, 200)
