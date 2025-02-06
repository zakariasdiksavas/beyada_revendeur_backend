
from base.models import Fournisseur, Site, Client


def get_fournisseur_by_user(request):
    return Fournisseur.objects.filter(revendeur=request.user.userext.revendeur.id).values('id')

def get_site_by_user(request):
    return Site.objects.filter(revendeur=request.user.userext.revendeur.id).values('id')

def get_batiments_by_user(request):
    return Site.objects.prefetch_related('batiment').filter(revendeur=request.user.userext.revendeur.id).values('batiments__id')

def get_clients_by_user(request):
    return Client.objects.filter(revendeur=request.user.userext.revendeur.id).only('id')