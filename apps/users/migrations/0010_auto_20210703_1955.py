# Generated by Django 3.2.4 on 2021-07-03 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_payment_payment_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='name',
            new_name='cnpj',
        ),
        migrations.AddField(
            model_name='payment',
            name='company_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]