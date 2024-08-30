from django.test import TestCase
from rest_framework.test import APIRequestFactory
from ..models import Menu
from ..views import MenuViewSet

class MenuViewSetTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu2 = Menu.objects.create(title="Pizza", price=120, inventory=50)

    def test_get_all_menus(self):
        factory = APIRequestFactory()
        request = factory.get('/menus/')
        view = MenuViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], self.menu1.title)
        self.assertEqual(response.data[1]['title'], self.menu2.title)