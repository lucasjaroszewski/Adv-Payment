from celery import shared_task
from django.core.mail import send_mail
from apps.users.models import Payment

@shared_task
def send_email_status(payment_status, email):
    send_mail('Payment status changed!',
              'Your payment status is now: ' + payment_status + '!',
              'adv.payment.jwt@gmail.com',
              [email])
