# Generated by Django 5.0.1 on 2024-01-26 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_foodsmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foodsmodel',
            options={'verbose_name': 'Food', 'verbose_name_plural': 'Foods'},
        ),
    ]
