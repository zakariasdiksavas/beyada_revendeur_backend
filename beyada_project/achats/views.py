from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import AchatSerializer
from .models import Achats
from django.shortcuts import get_object_or_404
from authentification.getters import get_batiments_by_user

# Create your views here.


# TODO Create achat
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_achat(request):
    """
    batiment -- int (required)
    quantity -- int (optional)
    poids_plateau -- float (optional)
    pu -- float (optional)
    date -- date (optional)
    classe -- int (optional)
    """
    # TODO Check if the batiment is related to the batiment of the user
    # batiments = [batiment.]
    serializer = AchatSerializer(data=request.data)
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
    user -- int (required)
    """
    data = request.data.copy()
    data['user'] = request.user.userext.id
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
    fournisseurs = Fournisseur.objects.filter(user=request.user.id)
    serializer = FournisseurSerializer(fournisseurs, many=True)
    return Response(serializer.data)