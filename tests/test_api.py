from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.users.models import User, Payment
from api.serializers import PaymentSerializer
import datetime as dt

# User creation data used in tests
user = {
    "name": "Lucas",
    "username": "Lucas",
    "email": "lucas@gmail.com",
    "password": "password123"
}

payment = {
    'user': 1,
    'email': 'lucas@gmail.com',
    'cnpj': '12.345.6789/0001-90',
    'company_name': 'Company',
    'price': 1000,
    'date_added': dt.date.today(),
    'expiration_date': "2021-07-21",
    'payment_status': 'Available'
}


class UserTests(APITestCase):

    def test_create_user(self):

        # Creating a new user
        url = reverse('user-register')
        self.client.post(url, user, format='json')
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 1)


    def authenticate(self):

        # Creates and authenticate the user
        self.client.post(reverse("user-register"), user, format='json')
        response = self.client.post(reverse('user-login'), {
            'email': 'lucas@gmail.com',
            'password': 'password123'
        })
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")


class PaymentTests(APITestCase):

    def test_create_payment(self):

        # Creating a new user
        self.client.post(reverse("user-register"), user, format='json')

        # Creating a new payment
        url = reverse('payment-create')
        self.client.post(url, payment, format='json')
        #self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Payment.objects.all().count(), 1)

    def test_update_payment(self):

        # Creating a new user
        self.client.post(reverse("user-register"), user, format='json')

        # Creating a new payment
        self.client.post(reverse("payment-create"), payment, format='json')

        # Payment_status changes to 'Pending'
        status = {'payment_status': 'Pending'}
        #self.client.post(reverse("payment-update/1"), status, format='json')
        #self.assertEqual({'payment_status': 'Pending'}, status)

    def test_deleting_payment(self):

        # Creating a new user
        self.client.post(reverse("user-register"), user, format='json')

        # Creating a new payment
        self.client.post(reverse("payment-create"), payment, format='json')

        # Deleting a payment
