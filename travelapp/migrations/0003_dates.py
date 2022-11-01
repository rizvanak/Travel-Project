# Generated by Django 4.0.5 on 2022-07-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('month', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='picture')),
                ('desc', models.TextField()),
            ],
        ),
    ]