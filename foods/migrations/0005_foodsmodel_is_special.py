# Generated by Django 5.0.1 on 2024-01-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_rename_image_foodsmodel_image1_foodsmodel_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodsmodel',
            name='is_special',
            field=models.BooleanField(default=True),
        ),
    ]
