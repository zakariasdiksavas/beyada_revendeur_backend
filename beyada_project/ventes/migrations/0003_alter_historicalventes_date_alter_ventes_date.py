# Generated by Django 5.1.5 on 2025-02-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0002_historicalventes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalventes',
            name='date',
            field=models.DateTimeField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='ventes',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
