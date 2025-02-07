# Generated by Django 5.1.5 on 2025-02-07 11:09

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_client_user_remove_historicalclient_user_and_more'),
        ('depense', '0002_maindoeuvre'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalMainDoeuvre',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('montant', models.FloatField()),
                ('date', models.DateField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('personnel', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='depense.personnel')),
            ],
            options={
                'verbose_name': 'historical main doeuvre',
                'verbose_name_plural': 'historical main doeuvres',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPersonnel',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cin', models.CharField(max_length=15)),
                ('inscription_nombre', models.IntegerField(blank=True, null=True)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('date_debut_travail', models.DateField(blank=True, null=True)),
                ('date_fin_travail', models.DateField(blank=True, null=True)),
                ('telephone', models.CharField(max_length=20)),
                ('addr', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('revendeur', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.revendeur')),
            ],
            options={
                'verbose_name': 'historical personnel',
                'verbose_name_plural': 'historical personnels',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTransport',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, 'Maintenance de vehicule'), (2, "Frias d'autoroute"), (3, 'Carburant'), (4, 'Autre')], default=4)),
                ('montant', models.FloatField()),
                ('date', models.DateField()),
                ('proof', models.TextField(blank=True, max_length=100, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('revendeur', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.revendeur')),
            ],
            options={
                'verbose_name': 'historical transport',
                'verbose_name_plural': 'historical transports',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(1, 'Maintenance de vehicule'), (2, "Frias d'autoroute"), (3, 'Carburant'), (4, 'Autre')], default=4)),
                ('montant', models.FloatField()),
                ('date', models.DateField()),
                ('proof', models.FileField(blank=True, null=True, upload_to='uploads/transport/proof/')),
                ('revendeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.revendeur')),
            ],
        ),
    ]
