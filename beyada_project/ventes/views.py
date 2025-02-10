from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import VenteSerializer
from .models import Ventes
from django.shortcuts import get_object_or_404
from authentification.getters import get_batiments_by_user, get_clients_by_user
from django.db.models import Q


# Create your views here.


# TODO Create vente
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_vente(request):
    """
    batiment -- int (required)
    client -- int (required)
    quantity -- int (optional)
    poids_plateau -- float (optional)
    pu -- float (optional)
    date -- date (optional)
    classe -- int (optional)
    """
    # TODO Check if the batiment is related to the batiment of the user
    batiments = [batiment['id'] for batiment in get_batiments_by_user(request)]
    if not request.data.get('batiment', None) in batiments:
        return Response({'error': "You are not able to add a vente with this batiment"}, status=status.HTTP_401_UNAUTHORIZED) 
    
    # TODO Check if the client is related to this user
    clients = [client.id for client in get_clients_by_user(request)]
    if not request.data.get('client', None) in clients:
        return Response({'error': "You are not able to add a vente with this client"}, status=status.HTTP_401_UNAUTHORIZED) 
    serializer = VenteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO Update vente
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_vente(request):
    """
    id -- int (required)
    batiment -- int (required)
    client -- int (required)
    quantity -- int (optional)
    poids_plateau -- float (optional)
    pu -- float (optional)
    date -- date (optional)
    classe -- int (optional)
    """
    # TODO Check if the batiment is related to the batiment of the user
    batiments = [batiment['id'] for batiment in get_batiments_by_user(request)]
    if not request.data.get('batiment', None) in batiments:
        return Response({'error': "You are not able to add a vente with this batiment"}, status=status.HTTP_401_UNAUTHORIZED) 
    # TODO Check if the client is related to this user
    clients = [client.id for client in get_clients_by_user(request)]
    if not request.data.get('client', None) in clients:
        return Response({'error': "You are not able to add a vente with this client"}, status=status.HTTP_401_UNAUTHORIZED) 
    vente = get_object_or_404(Ventes, pk=request.data['id'])
    serializer = VenteSerializer(vente, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete vente
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_vente(request):
    """
    id -- int (required)
    """
    vente = get_object_or_404(Ventes, pk=request.data['id'])
    vente.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# TODO List vente

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_vente(request):
    """
    id -- int 
    batiment -- int
    client -- int
    date1 -- date
    date2 -- date
    """
    filter = Q()
    params = request.query_params
    page_number = 2
    isInitial = True # todo Check if this is the initial request
    is_last = True # todo Check in pagination if this is the last item
    batiments = [batiment['id'] for batiment in get_batiments_by_user(request)]
    ventes = Ventes.objects.select_related('batiment', 'batiment__site', 'client')
    # TODO Filter data
    if params.get('batiment', None):
        isInitial = False
        batiments = [batiment for batiment in batiments if batiment == int(params.get('batiment'))]
    filter = Q(batiment__in=batiments)
    if params.get('client', None):
        filter &= Q(client=params.get('client'))
    if params.get('date1', None) and params.get('date2', None):
        isInitial = False
        filter &= Q(date__range=[params.get('date1'), params.get('date2')])
    elif params.get('date1', None):
        isInitial = False
        filter &= Q(date__gte=params.get('date1'))
    elif params.get('date2', None):
        isInitial = False
        filter &= Q(date__gte=params.get('date2'))
    if params.get('id', None):
        isInitial = False
        filter &= Q(id__lt=params.get('id'))
    ventes = ventes.filter(filter).order_by('-id')
    if (isInitial or params.get('id')) and len(ventes) > 0:
        ventes = ventes[:page_number]
        if not ventes[len(ventes) - 1].id == Ventes.objects.filter(filter).first().id:
            is_last = False
    serializer = VenteSerializer(ventes, many=True)
    return Response({'data': serializer.data, 'is_last': is_last})