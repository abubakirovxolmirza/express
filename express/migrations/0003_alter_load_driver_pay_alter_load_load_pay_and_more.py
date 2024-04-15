# Generated by Django 5.0.4 on 2024-04-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('express', '0002_alter_driver_tariff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='driver_pay',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True),
        ),
        migrations.AlterField(
            model_name='load',
            name='load_pay',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True),
        ),
        migrations.AlterField(
            model_name='load',
            name='per_mile',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True),
        ),
        migrations.AlterField(
            model_name='load',
            name='total_pay',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True),
        ),
    ]
