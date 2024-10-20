# Generated by Django 5.1.2 on 2024-10-19 02:22

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_alter_cart_product_variant'),
        ('products', '0006_alter_product_unique_together_product_is_returnable_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product_variant',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='products.productvariant'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
