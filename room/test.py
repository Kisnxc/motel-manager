from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from room.models import Room

class RoomTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.room = Room.objects.create(
            room_name='Phòng 101',
            room_price=1500000,
            owner=self.user
        )

    def test_room_str(self):
        self.assertEqual(str(self.room), 'Phòng 101 - 1500000 VNĐ')

    def test_room_list_view_requires_login(self):
        response = self.client.get(reverse('home'))  # trang danh sách phòng
        self.assertRedirects(response, '/accounts/login/?next=/')

    def test_room_list_view_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Phòng 101')

    def test_create_room_authenticated(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('room_create'), {
            'room_name': 'Phòng 102',
            'room_price': 2000000,
            'room_description': 'Phòng mới'
        })
        self.assertEqual(Room.objects.count(), 2)
        self.assertRedirects(response, reverse('home'))

    def test_create_room_unauthenticated(self):
        response = self.client.post(reverse('room_create'), {
            'room_name': 'Phòng 103',
            'room_price': 2500000,
            'room_description': 'Phòng test'
        })
        url = reverse('room_create')
        self.assertEqual(Room.objects.count(), 1)  # Chỉ có 1 phòng ban đầu
        self.assertRedirects(response, f'/accounts/login/?next={url}')
