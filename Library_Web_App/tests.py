from django.test import TestCase
from .models import Product

# Create your tests here.

class ModelTest(TestCase):
    def testProductModel(self):
        Smartphone = Product.objects.create(Name = "Xiaomi 12 Pro",Price = 45000)
        self.assertEqual(str(Smartphone) ,"Xiaomi 12 Pro")
        print("IsInstance:", isinstance(Smartphone,Product))
        self.assertTrue(isinstance(Smartphone,Product ))


#For testing a specific testcase use this command :- py manage.py test appname.tests
#for eg py manage.py test Library_Web_App.tests

