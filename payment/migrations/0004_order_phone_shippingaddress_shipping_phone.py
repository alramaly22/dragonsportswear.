# Generated by Django 5.1.4 on 2025-02-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_remove_order_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='shipping_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
