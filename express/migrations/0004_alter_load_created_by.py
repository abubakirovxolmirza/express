# Generated by Django 5.0.4 on 2024-04-16 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('express', '0003_alter_commodities_descriptions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='load',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dispatcher', to='express.dispatcher'),
            preserve_default=False,
        ),
    ]
