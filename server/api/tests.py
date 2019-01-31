import json

from rest_framework.test import APITestCase

from .models import Proxy


def prepare_proxies():

    proxy_list = [
        { 'name' : 'ws',   'rate' : 8 },
        { 'name' : 'pet',  'rate' : 9 },
        { 'name' : 'link', 'rate' : 0 },
        { 'name' : 'to',   'rate' : 1 },
    ]

    for proxy in proxy_list:
        test_proxy = Proxy(name = proxy['name'], rate = proxy['rate'])
        test_proxy.save()

    return proxy_list


class ProxyTests(APITestCase):

    def setUp(self):
        self.proxies = prepare_proxies()

    def test_proxies_order(self):
        response = self.client.get('/proxy/', format='json')
        proxies = json.loads( response.content )['results']
        
        for i in range( len(proxies) ):
            try:
                self.assertTrue( proxies[i]['rate'] > proxies[i+1]['rate'] )
            except IndexError:
                break

    def test_proxy_availability(self):
        for proxy in self.proxies:
            response = self.client.get('http://onion.{}'.format(proxy['name']))
            self.assertEqual(response.status_code, 200)