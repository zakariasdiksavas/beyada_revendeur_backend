from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import AchatSerializer
from .models import Achats
from django.shortcuts import get_object_or_404
from authentification.getters import get_batiments_by_user, get_fournisseur_by_user

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
    batiments = [batiment['batiments__id'] for batiment in get_batiments_by_user(request)]
    if not request.data['batiment'] in batiments:
        return Response({'error': "You are not able to add a achat with this batiment"}, status=status.HTTP_401_UNAUTHORIZED) 
    serializer = AchatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO Update achat
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_achat(request):
    """
    id -- int (required)
    batiment -- int (required)
    quantity -- int (optional)
    poids_plateau -- float (optional)
    pu -- float (optional)
    date -- date (optional)
    classe -- int (optional)
    """
    # TODO Check if the batiment is related to the batiment of the user
    batiments = [batiment['batiments__id'] for batiment in get_batiments_by_user(request)]
    if not request.data['batiment'] in batiments:
        return Response({'error': "You are not able to add a achat with this batiment"}, status=status.HTTP_401_UNAUTHORIZED) 
    achat = get_object_or_404(Achats, pk=request.data['id'])
    serializer = AchatSerializer(achat, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete achat
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_achat(request):
    """
    id -- int (required)
    """
    achat = get_object_or_404(Achats, pk=request.data['id'])
    achat.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# TODO List achat
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_achat(request):
    batiments = [batiment['batiments__id'] for batiment in get_batiments_by_user(request)]
    achats = Achats.objects.select_related('batiment', 'batiment__site').filter(batiment__in=batiments)
    serializer = AchatSerializer(achats, many=True)
    return Response(serializer.data)