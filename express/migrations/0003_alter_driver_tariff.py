# Generated by Django 5.0.4 on 2024-04-15 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('express', '0002_alter_driver_tariff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='tariff',
            field=models.FloatField(),
        ),
    ]
