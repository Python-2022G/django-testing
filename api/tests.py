from django.test import TestCase

from .models import Product


class ProductTestCase(TestCase):
    def test_create_model(self):
        product = Product.objects.create(
            name='p01',
            description='d01',
            price=9.7
        )

        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.first().name, 'p01')

