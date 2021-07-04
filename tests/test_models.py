from rest_framework.test import APITestCase
from apps.users.models import User, Payment
import unittest
import datetime as dt


# Creating user for testing
user = User(name='Lucas', email='lucas@gmail.com', password='password123')

class UserModelTests(APITestCase):

    def test_user_creation(self):
        self.assertIsInstance(user, User)

    def test_user_isStaff(self):
        self.assertFalse(user.is_staff)

    def test_user_email(self):
        self.assertEqual(user.email, 'lucas@gmail.com')

    def test_user_name(self):
        self.assertEqual(user.name, 'Lucas')

    def test_user_password(self):
        self.assertEqual(user.password, 'password123')

# Creating payment for testing
# Calculates the expiration date: today + 16 days
date = dt.date.today() + dt.timedelta(days=16)

payment = Payment(user=user,
                  cnpj='12.345.6789/0001-90',
                  company_name='Company',
                  price=1000,
                  date_added=dt.date.today(),
                  expiration_date=date,
                  payment_status='Available')


# Calculates expiration date - today = 16 days
days_left = (payment.expiration_date - dt.date.today()).days

# Calculates new price of payment
adv_payment = (payment.price - (payment.price * ((3/100) / 30) * days_left))


class PaymentModelTests(APITestCase):

    def test_payment_creation(self):
        self.assertIsInstance(payment, Payment)

    def test_payment_user(self):
        self.assertEqual(payment.user.email, 'lucas@gmail.com')

    def test_expiration_date(self):
        self.assertEqual(payment.expiration_date, date)

    def test_payment_status(self):
        self.assertEqual(payment.payment_status, 'Available')

    def test_days_left(self):
        self.assertEqual(days_left, 16)

    def test_adv_payment(self):
        self.assertNotEqual(adv_payment, 1000)
        self.assertEqual(adv_payment, 984)
