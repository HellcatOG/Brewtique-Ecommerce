# Generated by Django 5.1.1 on 2024-12-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_product_stock_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.TextField(default=0, verbose_name='Stock Quantity'),
        ),
    ]
