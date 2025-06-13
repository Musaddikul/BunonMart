# shop/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Category, SubCategory, Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Men")
        self.subcategory = SubCategory.objects.create(name="Shirts", category=self.category)
        self.product = Product.objects.create(
            name="Test Shirt",
            description="A test product",
            price=1200.00,
            image="products/test.jpg",
            category=self.category,
            subcategory=self.subcategory,
            section="men",
            is_featured=True
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Shirt")
        self.assertEqual(self.product.category.name, "Men")
        self.assertTrue(self.product.is_featured)

    def test_category_slug_autogeneration(self):
        self.assertEqual(self.category.slug, "men")

    def test_string_representation(self):
        self.assertEqual(str(self.product), "Test Shirt")
        self.assertEqual(str(self.category), "Men")
        self.assertEqual(str(self.subcategory), "Men > Shirts")


class ProductViewTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Women")
        Product.objects.create(
            name="Test Dress",
            description="Sample description",
            price=1500.00,
            image="products/dress.jpg",
            category=category,
            section="women",
        )

    def test_product_list_view(self):
        response = self.client.get(reverse("products"))  # you must have named the URL as 'products'
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Dress")
