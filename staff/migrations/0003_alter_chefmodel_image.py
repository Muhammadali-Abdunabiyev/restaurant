# Generated by Django 5.0.1 on 2024-01-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_rename_profesion_chefmodel_profession_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefmodel',
            name='image',
            field=models.ImageField(upload_to='chefs'),
        ),
    ]