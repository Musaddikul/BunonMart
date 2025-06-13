from django.test import TestCase
from .models import Product

class ProductTest(TestCase):
    def test_create_product(self):
        product = Product.objects.create(name="Shirt", price=500)
        self.assertEqual(product.name, "Shirt")

