from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.


class Personnel(models.Model):
    name = models.CharField(max_length=255)
    cin = models.CharField(max_length=15)
    inscription_nombre = models.IntegerField(blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    date_debut_travail = models.DateField(blank=True, null=True)
    date_fin_travail = models.DateField(blank=True, null=True)
    telephone = models.CharField(max_length=20)
    addr = models.CharField(max_length=255)
    revendeur = models.ForeignKey('base.Revendeur', on_delete=models.CASCADE)
    history = HistoricalRecords()


class MainDoeuvre(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.PROTECT, related_name='personnel')
    history = HistoricalRecords()
    montant = models.FloatField()
    date = models.DateField()
    history = HistoricalRecords()

class Transport(models.Model):
    CATEGORY = (
        (1, 'Maintenance de vehicule'),
        (2, "Frias d'autoroute"),
        (3, 'Carburant'),
        (4, 'Autre'),
    )
    category = models.IntegerField(choices=CATEGORY, default=4)
    montant = models.FloatField()
    date = models.DateField()
    proof = models.FileField(upload_to='uploads/transport/proof/', null=True, blank=True)
    revendeur = models.ForeignKey('base.Revendeur', on_delete=models.CASCADE)
    history = HistoricalRecords()

class Category(models.Model):
    name = models.CharField(max_length=255)
    revendeur = models.ForeignKey('base.Revendeur', on_delete=models.CASCADE)
    history = HistoricalRecords()


class Divers(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    montant = models.FloatField()
    date = models.DateField()
    proof = models.FileField(upload_to='uploads/divers/proof/', null=True, blank=True)
    history = HistoricalRecords()