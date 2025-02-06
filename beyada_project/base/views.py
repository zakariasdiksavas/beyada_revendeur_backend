from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import FournisseurSerializer, SiteSerializer,BatimentSerializer,ClientSerializer,ClientSelectSerializer
from .models import Fournisseur, Site, Batiment, Client
from django.shortcuts import get_object_or_404
from authentification.getters import get_fournisseur_by_user, get_batiments_by_user, get_site_by_user
# Create your views here.

# ============= TODO FOURNISSEUR ==============

# TODO Create fournisseur
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_fournisseur(request):
    """
    name -- str (required)
    address -- str (optional, max_length=200)
    phone -- str (optional, max_length=20)
    email -- str (optional)
    """
    data = request.data.copy()
    data['revendeur'] = request.user.userext.revendeur.id
    serializer = FournisseurSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO Update fournisseur
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_fournisseur(request):
    """
    id -- int (required)
    name -- str (required)
    address -- str (optional, max_length=200)
    phone -- str (optional, max_length=20)
    email -- str (optional)
    """
    data = request.data.copy()
    data['revendeur'] = request.user.userext.revendeur.id
    fournisseur = get_object_or_404(Fournisseur, pk=data['id'])
    serializer = FournisseurSerializer(fournisseur, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete fournisseur
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_fournisseur(request):
    """
    id -- int (required)
    """
    fournisseur = get_object_or_404(Fournisseur, pk=request.data['id'])
    fournisseur.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# TODO List fournisseur
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_fournisseur(request):
    fournisseurs = Fournisseur.objects.filter(revendeur=request.user.userext.revendeur)
    serializer = FournisseurSerializer(fournisseurs, many=True)
    return Response(serializer.data)

# ============= TODO Site ==============

# TODO Create site
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_site(request):
    """
    name -- str (required, max_length=50)
    address -- str (optional, max_length=200)
    phone -- str (optional, max_length=20)
    fournisseur -- int (required)
    """
    # TODO Check if the fournisseur id related to the fournisseur
    fournisseurs = [fournisseur['id'] for fournisseur in get_fournisseur_by_user(request)]

    if not request.data.get('fournisseur', -1) in fournisseurs:
        return Response({'error': "You are not able to add a site with this fournisseur"}, status=status.HTTP_401_UNAUTHORIZED)
    data = request.data.copy()
    data['revendeur'] = request.user.userext.revendeur.id
    serializer = SiteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO Update site
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_site(request):
    """
    id -- int (required)
    name -- str (required, max_length=50)
    address -- str (optional, max_length=200)
    phone -- str (optional, max_length=20)
    fournisseur -- int (required)
    """
    # TODO Check if the fournisseur id related to the fournisseur
    fournisseurs = [fournisseur['id'] for fournisseur in get_fournisseur_by_user(request)]
    if not request.data['fournisseur'] in fournisseurs:
        return Response({'error': "You are not able to add a site with this fournisseur"}, status=status.HTTP_401_UNAUTHORIZED)
    site = get_object_or_404(Site, pk=request.data['id'])
    data = request.data.copy()
    data['revendeur'] = request.user.userext.revendeur
    serializer = SiteSerializer(site, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete site
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_site(request):
    """
    id -- int (required)
    """
    site = get_object_or_404(Site, pk=request.data['id'])
    site.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# TODO List sites
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_site(request):
    site = Site.objects.prefetch_related('fournisseur').filter(revendeur=request.user.userext.revendeur.id)
    serializer = SiteSerializer(site, many=True)
    return Response(serializer.data)

# ============= TODO Batiment ==============

# TODO Create batiment
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_batiment(request):
    """
    site -- int (required)
    name -- str (required, max_length=100)
    """
    # TODO Check if the batiment id related to the site
    sites = [fournisseur['id'] for fournisseur in get_site_by_user(request)]
    if not request.data['site'] in sites:
        return Response({'error': "You are not able to add a batiment with this site"}, status=status.HTTP_401_UNAUTHORIZED)
    serializer = BatimentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO Update batiment
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_batiment(request):
    """
    id -- int (required)
    site -- int (required)
    name -- str (required, max_length=100)
    """
     # TODO Check if the batiment id related to the site
    sites = [fournisseur['id'] for fournisseur in get_site_by_user(request)]
    if not request.data['site'] in sites:
        return Response({'error': "You are not able to add a batiment with this site"}, status=status.HTTP_401_UNAUTHORIZED)
    batiment = get_object_or_404(Batiment, pk=request.data['id'])
    serializer = BatimentSerializer(batiment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete batiment
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_batiment(request):
    """
    id -- int (required)
    """
    batiment = get_object_or_404(Batiment, pk=request.data['id'])
    batiment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# TODO List sites
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_batiment(request):
    sites = [fournisseur['id'] for fournisseur in get_site_by_user(request)]
    batiments = Batiment.objects.select_related('site').filter(site__in=sites)
    serializer = BatimentSerializer(batiments, many=True)
    return Response(serializer.data)
 
# ============= TODO CLIENT ==============

# TODO Create client
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_client(request):
    """
    name -- str (required, max_length=100)
    address -- str (optional, max_length=200)
    phone -- str (optional, max_length=20)
    email -- str (optional)
    is_passager -- bool (default=False)
    is_active -- bool (default=True)
    """
    data = request.data.copy()
    data['revendeur'] = request.user.userext.revendeur.id
    serializer = ClientSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO Update client
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_client(request):
    """
    id -- id (required)
    name -- str (required, max_length=100)
    address -- str (optional, max_length=200)
    phone -- str (optional, max_length=20)
    email -- str (optional)
    is_passager -- bool (default=False)
    is_active -- bool (default=True)
    """
    data = request.data.copy()
    data['revendeur'] = request.user.userext.revendeur.id
    client = get_object_or_404(Client, pk=data['id'])
    serializer = ClientSerializer(client, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete client
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_client(request):
    """
    id -- id (required)
    """
    client = get_object_or_404(Client, pk=request.data['id'])
    client.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# TODO List client
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_client(request):
    client = Client.objects.filter(revendeur=request.user.userext.revendeur.id)
    serializer = ClientSerializer(client, many=True)
    return Response(serializer.data)


# TODO List select fournisseur and site and batiment
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_select_data(request):
    data = Fournisseur.objects.prefetch_related('site').filter(user=request.user.userext.id)
    data_dict = [{'id': fournisseur.id, 'name': fournisseur.name,
                'site': [{"id" : site.id, "name": site.name, 
                "batiments": site.batiments.select_related('batiments').all().values('id', 'name')} 
                for site in fournisseur.site.prefetch_related('batiments').all()]} 
                for fournisseur in data ]
    return Response(data_dict)

# TODO List select client
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_select_client(request):
    client = Client.objects.filter(user=request.user.userext.id)
    serializer = ClientSelectSerializer(client, many=True)
    return Response(serializer.data)

