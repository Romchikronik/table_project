# Generated by Django 4.1.5 on 2023-01-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_loiha41_time_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loiha41',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания'),
        ),
    ]
