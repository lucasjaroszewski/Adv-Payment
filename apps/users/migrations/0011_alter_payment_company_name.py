# Generated by Django 3.2.4 on 2021-07-03 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210703_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='company_name',
            field=models.CharField(max_length=255),
        ),
    ]
