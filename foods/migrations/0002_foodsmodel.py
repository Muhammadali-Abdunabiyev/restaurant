# Generated by Django 5.0.1 on 2024-01-26 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='foods')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Foods',
                'verbose_name_plural': 'Foods',
            },
        ),
    ]
