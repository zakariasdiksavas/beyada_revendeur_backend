from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import PaimentVenteSerializer, PaimentClientSerializer, PaiementProofSerializer
from .models import Paiment, PaiementProof
from django.shortcuts import get_object_or_404
from authentification.getters import get_clients_by_user
from .functions import *

# Create your views here.

# ? ================= PAIMENT VENTE ==================== #

# TODO Create paimentVente
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_paimentVente(request):
    """
    client_vente -- int (required) -- id of client
    vente -- int (required)
    status -- int (optional)
    paiement_mode -- int (optional)
    montant -- float (optional)
    date -- date (optional)
    """
    
    # TODO Check if the client is related to this user
    clients = [client.id for client in get_clients_by_user(request)]
    if not request.data['client_vente'] in clients:
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
    client_vente -- int (required) -- id of client
    vente -- int (required)
    status -- int (optional)
    paiement_mode -- int (optional)
    montant -- float (optional)
    date -- date (optional)
    """
    # TODO Check if the batiment is related to the batiment of the user
    # TODO Check if the client is related to this user
    clients = [client.id for client in get_clients_by_user(request)]
    if not request.data['client_vente'] in clients:
        return Response({'error': "You are not able to add a paimentVente with this client"}, status=status.HTTP_401_UNAUTHORIZED) 
    paimentVente = get_object_or_404(Paiment, pk=request.data['id'])
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
    paimentVente = get_object_or_404(Paiment, pk=request.data['id'])
    paimentVente.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# TODO List paimentVente
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_paimentVente(request):
    vente = request.query_params.get('vente', None)
    if not vente:
        return Response({"error": "Mismatch of vente id"}, status=status.HTTP_404_NOT_FOUND)
    paimentVentes = Paiment.objects.filter(vente=vente)
    serializer = PaimentVenteSerializer(paimentVentes, many=True, context={'request': request})
    return Response(serializer.data)

# TODO Update status paiment
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_paiment_status_vente(request):
    """
    id -- int (required)
    status -- int (required)
    """
    id = request.data.get('id', None)
    statut = request.data.get('status', None)
    if id and statut:
        paimentVente = get_object_or_404(Paiment, pk=id)
        paimentVente.status = statut
        paimentVente.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    
# ? ================= PAIMENT CLIENT ==================== #
    

# TODO Create Paimentclient
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_paimentClient(request):
    """
    client_client -- int (required) -- id of client
    status -- int (optional)
    paiement_mode -- int (optional)
    montant -- float (optional)
    date -- date (optional)
    """
    
    # TODO Check if the client is related to this user
    clients = [client.id for client in get_clients_by_user(request)]
    if not request.data['client_client'] in clients:
        return Response({'error': "You are not able to add a paiment Client with this client"}, status=status.HTTP_401_UNAUTHORIZED) 
    serializer = PaimentClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO Update paimentClient
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_paimentClient(request):
    """
    id -- int (required)
    client_client -- int (required) -- id of client
    vente -- int (required)
    status -- int (optional)
    paiement_mode -- int (optional)
    montant -- float (optional)
    date -- date (optional)
    """
    # TODO Check if the batiment is related to the batiment of the user
    # TODO Check if the client is related to this user
    clients = [client.id for client in get_clients_by_user(request)]
    if not request.data['client_client'] in clients:
        return Response({'error': "You are not able to add a paiment Client with this client"}, status=status.HTTP_401_UNAUTHORIZED) 
    paimentClient = get_object_or_404(Paiment, pk=request.data['id'])
    serializer = PaimentClientSerializer(paimentClient, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete paimentClient
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_paimentClient(request):
    """
    id -- int (required)
    """
    paimentClient = get_object_or_404(Paiment, pk=request.data['id'])
    paimentClient.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# TODO List paimentClient
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_paimentClient(request):
    client = request.query_params.get('client', None)
    if not client:
        return Response({"error": "Mismatch of client id"}, status=status.HTTP_404_NOT_FOUND)
    paimentClients = Paiment.objects.prefetch_related('paiment').filter(client_client=client)
    serializer = PaimentClientSerializer(paimentClients, many=True, context={'request': request})
    return Response(serializer.data)

# TODO Update status paiment
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_paiment_status_client(request):
    """
    id -- int (required)
    status -- int (required)
    """
    id = request.data.get('id', None)
    statut = request.data.get('status', None)
    if id and status:
        paimentClient = get_object_or_404(Paiment, pk=id)
        paimentClient.status = statut
        paimentClient.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# ? ================= PAIMENT proof ==================== #


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_payment_try_proof(request):
    """
    paiment -- id of payment try
    file -- uploaded file (allowed_extensions = ['jpg','jpeg','png'])
    """
    file = request.FILES.get('file')
    if not is_image_extension_valid(file):
        return Response({"image format is not valid"}, status=status.HTTP_400_BAD_REQUEST)
    
    file = resize_image(file, 800)
    data = {
        "paiment": request.data.get("paiment"),
        "file": file,
    }
    serializer = PaiementProofSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_payment_try_proof(request):
    """
    id -- id of payment proof
    file -- uploaded file (allowed_extensions = ['jpg','jpeg','png'])
    """
    #get instance
    instance = get_object_or_404(PaiementProof, id=request.data.get("id"))
    
    #verify file existance
    file = request.FILES.get('file')
    if not file:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #check file extension
    if not is_image_extension_valid(file):
        return Response({"error: image format is not valid"}, status=status.HTTP_400_BAD_REQUEST)
    
    #resize file
    file = resize_image(file, 800)
    data = {
        "paiment": request.data.get("paiment"),
        "file": file,
    }
    serializer = PaiementProofSerializer(instance=instance, data=data, partial=True)
    if serializer.is_valid():
        instance.file.delete()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_payment_try_proof(request):
    """
    id -- id of payment proof
    """
    #get instance
    instance = get_object_or_404(PaiementProof, id=request.data.get("id"))
    instance.file.delete()
    instance.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
