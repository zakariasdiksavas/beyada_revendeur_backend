from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import VenteSerializer
from .models import Ventes
from django.shortcuts import get_object_or_404
from authentification.getters import get_batiments_by_user, get_clients_by_user

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
    batiments = [batiment['batiments__id'] for batiment in get_batiments_by_user(request)]
    if not request.data['batiment'] in batiments:
        return Response({'error': "You are not able to add a vente with this batiment"}, status=status.HTTP_401_UNAUTHORIZED) 
    
    # TODO Check if the client is related to this user
    clients = [client.id for client in get_clients_by_user(request)]
    if not request.data['client'] in clients:
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
    batiments = [batiment['batiments__id'] for batiment in get_batiments_by_user(request)]
    if not request.data['batiment'] in batiments:
        return Response({'error': "You are not able to add a vente with this batiment"}, status=status.HTTP_401_UNAUTHORIZED) 
    # TODO Check if the client is related to this user
    clients = [client.id for client in get_clients_by_user(request)]
    if not request.data['client'] in clients:
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
    batiments = [batiment['batiments__id'] for batiment in get_batiments_by_user(request)]
    ventes = Ventes.objects.select_related('batiment', 'batiment__site', 'client').filter(batiment__in=batiments)
    serializer = VenteSerializer(ventes, many=True)
    return Response(serializer.data)