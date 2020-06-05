from django.test import TestCase
from .models import *

class TestModels(TestCase):
    def test_str_to_return_name_for_category(self):
        test_category = Category.objects.create(name="test_category")
        self.assertEqual(str(test_category), test_category.name)

    def test_str_to_return_name_for_subcategory(self):
        test_subcategory = SubCategory.objects.create(name="test_subcategory")
        self.assertEqual(str(test_subcategory), test_subcategory.name)

    def test_str_to_return_name_for_Product(self):
        test_product = Product.objects.create(name="test_product", stock=1, price=1)
        self.assertEqual(str(test_product), test_product.name)