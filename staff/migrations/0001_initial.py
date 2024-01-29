# Generated by Django 5.0.1 on 2024-01-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChefModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='chef')),
                ('name', models.CharField(max_length=255)),
                ('profesion', models.CharField(max_length=221)),
                ('info', models.CharField(max_length=225)),
                ('instagram', models.URLField()),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Chef',
                'verbose_name_plural': 'Chefs',
            },
        ),
    ]
