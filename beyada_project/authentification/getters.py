
from base.models import *
from django.db.models import F

def get_fournisseur_by_user(request):
    return Fournisseur.objects.filter(revendeur=request.user.userext.revendeur.id).values('id')

def get_site_by_user(request):
    return Fournisseur.objects.prefetch_related('site').filter(revendeur=request.user.userext.revendeur.id).values('site__id').annotate(id=F('site__id'))

def get_batiments_by_user(request):
    return Batiment.objects.select_related('site', 'site__fournisseur').filter(site__fournisseur__revendeur=request.user.userext.revendeur.id).values('id')

def get_clients_by_user(request):
    return Client.objects.filter(revendeur=request.user.userext.revendeur.id).only('id')