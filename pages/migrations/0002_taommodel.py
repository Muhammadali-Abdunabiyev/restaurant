# Generated by Django 5.0.1 on 2024-01-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=221)),
                ('left_image', models.ImageField(upload_to='')),
                ('right_image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
            ],
        ),
    ]
