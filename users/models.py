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

    # Description
    name = models.CharField(max_length=255)
    price = models.FloatField()
    date_added = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()

    def save(self, *args, **kwargs):
        super(Payment, self).save(*args, **kwargs)

    def days_left(self):
        return (self.expiration_date - dt.date.today()).days

    def __str__(self):
        return f'User: {self.user} ({self.user.id}) - {self.name}'
