# Generated by Django 5.1.2 on 2024-10-19 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
        ('products', '0006_alter_product_unique_together_product_is_returnable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coupons', to='products.category'),
        ),
        migrations.AlterField(
            model_name='couponvariant',
            name='coupon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='coupons.coupon'),
        ),
        migrations.AlterField(
            model_name='couponvariant',
            name='productVariant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to='products.productvariant'),
        ),
    ]
