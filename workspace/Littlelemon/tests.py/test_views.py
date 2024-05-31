from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Coffee", price=20, inventory=100)

    def test_getall(self):
        data = Menu.objects.all()
        serializer = MenuSerializer(data,many=True)
        self.assertTrue(serializer)
        
        

    