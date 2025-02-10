from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import *

# Create your views here.


# TODO Create command
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_commande(request):
    """
    batiment -- int (required)
    client -- int (required)
    quantity -- int (required)
    poids_plateau -- float (required)
    pu -- float (required)
    description -- str (required, max_length=200)
    is_delivered -- bool (default=False)
    date -- date (optional)
    classe -- int (optional)
    """
    data = request.data.copy()
    data['created_by'] = request.user.id
    serializer = CommandSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
