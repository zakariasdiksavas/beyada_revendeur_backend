
from base.models import Fournisseur, Site

def get_fournisseur_by_user(request):
    return Fournisseur.objects.prefetch_related('site').filter(user=request.user.userext.id).values('site__id', 'id')

def get_batiments_by_user(request):
    fournisseurs =  Fournisseur.objects.prefetch_related('site').filter(user=request.user.userext.id).values('site__id')
    batiments = Site.objects.filter(fournisseur__in=fournisseurs).prefetch_related('batiments').values('batiments') # TODO STILL WORKING HERE
    return batiments