# Generated by Django 5.1.2 on 2024-10-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_rename_likes_productreview_likes_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
