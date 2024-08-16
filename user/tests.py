from django.contrib.auth.models import User
from django.test import TestCase, Client


class TestUser(TestCase):
    fixtures = ['data']

    def setUp(self):
        self.test_user = User.objects.create_user(username='test_user', password='test_password')

    def test_registration(self):
        actual_user = User.objects.get(pk=self.test_user.pk)
        self.assertEqual(actual_user.username, 'test_user')
        print(f'User {actual_user.username} was created')

    def test_login(self):
        c = Client()
        c.login(username='test_user', password='test_password')
        response = c.post('/user/login/')
        self.assertEqual(response.status_code, 200)
        print(f'User {self.test_user.username} logged in')

