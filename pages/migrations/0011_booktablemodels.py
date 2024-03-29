# Generated by Django 5.0.1 on 2024-01-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_emailmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTableModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
                ('no_of_people', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('time', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'BookTable',
                'verbose_name_plural': 'BookTables',
            },
        ),
    ]
