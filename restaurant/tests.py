from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Menu, Booking
from django.utils import timezone

class MenuTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        Menu.objects.create(title='Bruschetta', price=11.00, inventory=50)
        Menu.objects.create(title='Greek Salad', price=12.00, inventory=30)

    def test_get_menu_items(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_create_menu_item(self):
        data = {'title': 'Grilled Fish', 'price': '9.00', 'inventory': 20}
        response = self.client.post('/api/menu/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Menu.objects.count(), 3)

    def test_get_single_menu_item(self):
        item = Menu.objects.first()
        response = self.client.get(f'/api/menu/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], item.title)

    def test_update_menu_item(self):
        item = Menu.objects.first()
        data = {'title': 'Updated Item', 'price': '15.00', 'inventory': 10}
        response = self.client.put(f'/api/menu/{item.id}/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Item')

    def test_delete_menu_item(self):
        item = Menu.objects.first()
        response = self.client.delete(f'/api/menu/{item.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Menu.objects.count(), 1)

    def test_unauthenticated_access(self):
        client = APIClient()
        response = client.get('/api/menu/')
        self.assertEqual(response.status_code, 401)

class BookingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        Booking.objects.create(
            name='John Doe',
            no_of_guests=2,
            booking_date=timezone.now()
        )

    def test_get_bookings(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_booking(self):
        data = {
            'name': 'Jane Doe',
            'no_of_guests': 4,
            'booking_date': '2025-12-25T19:00:00Z'
        }
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 2)

    def test_get_single_booking(self):
        booking = Booking.objects.first()
        response = self.client.get(f'/api/bookings/{booking.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_delete_booking(self):
        booking = Booking.objects.first()
        response = self.client.delete(f'/api/bookings/{booking.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Booking.objects.count(), 0)

class RegistrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        data = {'username': 'newuser', 'email': 'new@test.com', 'password': 'newpass123'}
        response = self.client.post('/api/registration/', data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('token', response.data)

    def test_get_token(self):
        User.objects.create_user(username='tokenuser', password='tokenpass')
        data = {'username': 'tokenuser', 'password': 'tokenpass'}
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)
