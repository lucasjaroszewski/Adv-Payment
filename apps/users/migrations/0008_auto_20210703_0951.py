# Generated by Django 3.2.4 on 2021-07-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(choices=[('AVAILABLE', 'Available'), ('EXPIRED', 'Expired'), ('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('DENIED', 'Denied')], default='Available', max_length=10),
        ),
    ]
