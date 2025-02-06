from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import PaimentVenteSerializer
from .models import PaimentByVente
from django.shortcuts import get_object_or_404
from authentification.getters import get_clients_by_user


# Create your views here.


# TODO Create paimentVente
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_paimentVente(request):
    """
    batiment -- int (required)
    client_vente -- int (required) -- id of client
    quantity -- int (optional)
    poids_plateau -- float (optional)
    pu -- float (optional)
    date -- date (optional)
    classe -- int (optional)
    """
    
    # TODO Check if the client is related to this user
    clients = [client.id for client in get_clients_by_user(request)]
    if not request.data['client'] in clients:
        return Response({'error': "You are not able to add a paimentVente with this client"}, status=status.HTTP_401_UNAUTHORIZED) 
    serializer = PaimentVenteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO Update paimentVente
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_paimentVente(request):
    """
    id -- int (required)
    batiment -- int (required)
    client_vente -- int (required) -- id of client
    quantity -- int (optional)
    poids_plateau -- float (optional)
    pu -- float (optional)
    date -- date (optional)
    classe -- int (optional)
    """
    # TODO Check if the batiment is related to the batiment of the user
    # TODO Check if the client is related to this user
    clients = [client.id for client in get_clients_by_user(request)]
    if not request.data['client'] in clients:
        return Response({'error': "You are not able to add a paimentVente with this client"}, status=status.HTTP_401_UNAUTHORIZED) 
    paimentVente = get_object_or_404(PaimentByVente, pk=request.data['id'])
    serializer = PaimentVenteSerializer(paimentVente, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete paimentVente
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_paimentVente(request):
    """
    id -- int (required)
    """
    paimentVente = get_object_or_404(PaimentByVente, pk=request.data['id'])
    paimentVente.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# TODO List paimentVente
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_paimentVente(request):
    vente = request.query_params.get('vente', None)
    if not vente:
        return Response({"error": "Mismatch of vente id"}, status=status.HTTP_404_NOT_FOUND)
    paimentVentes = PaimentByVente.objects.filter(vente=request.query_params.get('vente'))
    serializer = PaimentVenteSerializer(paimentVentes, many=True)
    return Response(serializer.data)

# TODO Update status paiment
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_paiment_status(request):
    """
    id -- int (required)
    status -- int (required)
    """
    id = request.data.get('id', None)
    paiement_mode = request.data.get('paiement_mode', None)
    if id and paiement_mode:
        paimentVente = get_object_or_404(PaimentByVente, pk=id)
        paimentVente.paiement_mode = paiement_mode
        paimentVente.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    

    