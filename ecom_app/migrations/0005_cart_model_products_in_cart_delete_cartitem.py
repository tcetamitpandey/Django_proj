# Generated by Django 5.0.2 on 2024-03-07 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0004_remove_cart_model_products_in_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_model',
            name='products_in_cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecom_app.product_model'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
