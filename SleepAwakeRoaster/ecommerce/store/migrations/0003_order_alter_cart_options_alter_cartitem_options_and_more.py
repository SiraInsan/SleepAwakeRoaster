# Generated by Django 5.0.4 on 2024-04-22 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cart_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('address', models.CharField(max_length=255, unique=True)),
                ('city', models.CharField(max_length=255, unique=True)),
                ('postcode', models.CharField(max_length=255, unique=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email', models.EmailField(blank=True, max_length=250)),
                ('token', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('date_added',), 'verbose_name': 'ตะกร้าสินค้า', 'verbose_name_plural': 'ข้อมูลตะกร้าสินค้า'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'รายการสินค้าในตะกร้า', 'verbose_name_plural': 'ข้อมูลรายการสินค้าในตะกร้า'},
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
    ]
