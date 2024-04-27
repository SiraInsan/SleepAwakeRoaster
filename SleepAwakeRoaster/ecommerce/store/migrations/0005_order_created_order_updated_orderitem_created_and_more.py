# Generated by Django 5.0.4 on 2024-04-22 12:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_order_options_alter_orderitem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
