# Generated by Django 5.1.5 on 2025-02-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0003_alter_historicalventes_date_alter_ventes_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalventes',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ventes',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
