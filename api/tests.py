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

