# Generated by Django 5.0.4 on 2024-04-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('express', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='tariff',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
