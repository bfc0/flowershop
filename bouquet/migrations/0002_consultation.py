# Generated by Django 5.1.1 on 2024-09-20 13:52

import django.utils.timezone
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bouquet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, verbose_name='Имя клиента')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Номер телефона')),
                ('registration_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время регистрации')),
                ('order_accepted', models.BooleanField(default=False, verbose_name='Заказ принят')),
            ],
            options={
                'verbose_name': 'Консультация',
                'verbose_name_plural': 'Консультации',
            },
        ),
    ]
