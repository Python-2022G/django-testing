from django.test import TestCase

from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        product = Product.objects.create(
            name='p01',
            description='d01',
            price=9.7
        )

    def test_attribute(self):

        self.assertEqual(Product.objects.first().name, 'p01')

    def test_count(self):

        self.assertEqual(Product.objects.count(), 1)

class ProductListViewTestCase(TestCase):
    def test_getting_products(self):
        Product.objects.create(
            name='p01',
            description='d01',
            price=9.7
        )

        response = self.client.get('/api/products/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"id": 1, "name": "p01", "description": "d01", "price": 9.7}])

    def test_create_product(self):
        data = {
            "name": "p02",
            "description": "d02",
            "price": 8.3
        }

        response = self.client.post('/api/products/', data=data, content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            "id": 1,
            "name": "p02",
            "description": "d02",
            "price": 8.3
        })
