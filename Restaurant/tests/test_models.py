from django.test import TestCase
from Restaurant.models import Menu, MenuItem, Booking

class MenuTest(TestCase):
    def test_str_representation(self):
        print("Ejecutando prueba...")
        item = Menu(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")