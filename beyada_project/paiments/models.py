from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class PaimentByVente(models.Model):
    client_vente = models.ForeignKey('base.Client', on_delete=models.PROTECT, related_name='client_vente', null=True, blank=True)
    client_client = models.ForeignKey('base.Client', on_delete=models.PROTECT, related_name='client_client', null=True, blank=True)
    vente = models.ForeignKey('ventes.Ventes', on_delete=models.PROTECT, null=True, blank=True)
    PAYMENT_STATUS = (
        (1, 'en cours'),
        (2, 'payé'),
        (3, 'échec'),
    )
    status = models.IntegerField(choices=PAYMENT_STATUS, default=1)
    PAIEMENT_MODES = (
        (1, 'Espéce'),
        (2, 'Chèque'),
        (3, 'LCN'),
        (4, 'Virement'),
    )
    paiement_mode = models.IntegerField(choices=PAIEMENT_MODES, default=1)
    montant = models.FloatField()
    date = models.DateField(auto_now=True)
    history = HistoricalRecords()


# class PaiementProof(models.Model):
#     paiement_try = models.ForeignKey(PaimentByVente, related_name='proofs', on_delete=models.CASCADE)
#     file = models.ImageField(upload_to='uploads/paiements/proofs/')
#     history = HistoricalRecords()
    
