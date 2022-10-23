from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from core import models
from rest_framework import status



class Register(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_not_allowed(self):
        response = self.client.get(reverse({"core:user_register"}))
        self.assertEqual(response.status_code, 200)

    def test_success_registration(self):
        data = {'username': 'test_user', 'password': '12345678'}
        response = self.client.post(
            path=reverse('core:user_register'),
            data=data,
        )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        user = models.User.objects.filter(username=data['username']).first()
        self.assertTrue(user)
        self.assertTrue(user.check_password(data['password']))
