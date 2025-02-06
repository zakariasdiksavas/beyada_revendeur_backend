# Generated by Django 5.1.5 on 2025-02-06 10:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0003_remove_userext_fournisseur'),
        ('base', '0008_revendeur_remove_fournisseur_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluserext',
            name='revendeur',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.revendeur'),
        ),
        migrations.AddField(
            model_name='userext',
            name='fournisseur',
            field=models.ManyToManyField(to='base.fournisseur'),
        ),
        migrations.AddField(
            model_name='userext',
            name='revendeur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.revendeur'),
        ),
    ]
