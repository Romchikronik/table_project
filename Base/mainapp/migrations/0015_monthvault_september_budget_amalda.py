# Generated by Django 4.1.5 on 2023-02-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_alter_kunliu_options_tarmokvault_rejavault_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthvault',
            name='september_budget_amalda',
            field=models.CharField(default='', max_length=255, verbose_name='Режа'),
        ),
    ]