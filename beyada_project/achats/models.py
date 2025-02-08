from django.db import models
from simple_history.models import HistoricalRecords
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Achats(models.Model):
    batiment = models.ForeignKey('base.Batiment', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    poids_plateau = models.FloatField(default=0, null=False, blank=False)
    pu = models.FloatField(default=0, null=False, blank=False)
    date = models.DateField(default=timezone.now)
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
