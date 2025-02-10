from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.


class Ventes(models.Model):
    batiment = models.ForeignKey('base.Batiment', on_delete=models.PROTECT, db_index=True)
    client = models.ForeignKey('base.Client', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    poids_plateau = models.FloatField(default=0, null=False, blank=False)
    pu = models.FloatField(default=0, null=False, blank=False)
    date = models.DateTimeField()
    CLASSES = (
        (1, "normal"),
        (2, "double jaune"),
        (3, "blanc"),
        (4, "sale"),
        (5, "casse"),
        (6, "elimine"),
        (7, "triage"),
    )
    classe = models.IntegerField(choices=CLASSES, default=1)
    history = HistoricalRecords()
