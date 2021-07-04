from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime as dt


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Payment(models.Model):

    # User authentication
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')

    # Payment status
    PAYMENT_STATUS = (
        ('Available', 'Available'),
        ('Expired', 'Expired'),
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Denied', 'Denied')
    )

    # Details
    cnpj = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    price = models.FloatField()
    date_added = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='Available')

    def save(self, *args, **kwargs):
        super(Payment, self).save(*args, **kwargs)


    # Calculates how many days there is until expiration date
    def days_left(self):
        return (self.expiration_date - dt.date.today()).days


    # Calculates new price to pay by antecipating the payment
    def adv_payment(self):
        days_left = (self.expiration_date - dt.date.today()).days

        if days_left < 0:
            return f'Expired'

        adv_payment = (self.price - (self.price * ((3/100) / 30) * days_left))
        return adv_payment


    def __str__(self):
        return f'User: {self.user} ({self.user.id}) - {self.company_name}'
