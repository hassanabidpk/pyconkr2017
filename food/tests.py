from django.test import TestCase, Client
from food.models import Restaurant
from django.contrib.auth.models import User


class RestaurantTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        writer = User.objects.create_user('test_user', \
        'test@example.com', 'password1')
        rest = Restaurant.objects.create(name="kfc", \
        address="seoul", menu="burger", tags="burger", writer=writer)

    def test_restaurant_has_name(self):
        """Restaurant object is created Ok with a name """
        rest = Restaurant.objects.get(name="kfc")
        self.assertEqual(rest.name, "kfc")

    def test_index_page(self):
        "Check if new restaurant is added to index page"
        response = self.client.get("/")
        self.assertContains(response, "kfc")

