from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializer import *
from paiments.functions import *



# ? ================= Personnel ==================== #

# TODO Create personnel
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_personnel(request):
    """
    name -- str (required, max_length=255)
    cin -- str (required, max_length=15)
    inscription_nombre -- int (optional)
    date_naissance -- date (optional)
    date_debut_travail -- date (optional)
    date_fin_travail -- date (optional)
    telephone -- str (required, max_length=20)
    addr -- str (required, max_length=255)
    """
    data = request.data.copy()
    data['revendeur'] = request.user.userext.revendeur.id
    serializer = PersonnelSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# TODO Update personnel
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_personnel(request):
    """
    id -- id (required)
    name -- str (required, max_length=255)
    cin -- str (required, max_length=15)
    inscription_nombre -- int (optional)
    date_naissance -- date (optional)
    date_debut_travail -- date (optional)
    date_fin_travail -- date (optional)
    telephone -- str (required, max_length=20)
    addr -- str (required, max_length=255)
    """
    data = request.data.copy()
    data['revendeur'] = request.user.userext.revendeur.id
    personnel = get_object_or_404(Personnel, pk=data['id'])
    serializer = PersonnelSerializer(personnel, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete personnel
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_personnel(request):
    """
    id -- id (required)
    """
    personnel = get_object_or_404(Personnel, pk=request.data.get('id', None))
    personnel.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_personnel(request):
    personnel = Personnel.objects.filter(revendeur=request.user.userext.revendeur.id).values()
    return Response(personnel)



# ? ================= MAIN D'OEUVRE DEPENSE ==================== #

# TODO Create maindoeuvre
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_maindoeuvre(request):
    """
    personnel -- int (required)
    montant -- float (required)
    date -- date (required)
    """
    serializer = MainDoeuvreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# TODO Update maindoeuvre
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_maindoeuvre(request):
    """
    id -- int (required)
    personnel -- int (required)
    montant -- float (required)
    date -- date (required)
    """
    maindoeuvre = get_object_or_404(MainDoeuvre, pk=request.data['id'])
    serializer = MainDoeuvreSerializer(maindoeuvre, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete maindoeuvre
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_maindoeuvre(request):
    """
    id -- id (required)
    """
    maindoeuvre = get_object_or_404(MainDoeuvre, pk=request.data.get('id', None))
    maindoeuvre.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_maindoeuvre(request):
    personnel = MainDoeuvre.objects.filter(personnel__revendeur=request.user.userext.revendeur.id)
    serializer = MainDoeuvreSerializer(personnel, many=True)
    return Response(serializer.data)


# ? ================= TRANSPORT ==================== #

# TODO Create transport
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_transport(request):
    """
    category -- int (optionnal)
    montant -- float (required)
    date -- date (required)
    proof -- file (optionnal)
    """
    data = request.data.copy()
    file = request.FILES.get('proof')
    if file:
            if not is_image_extension_valid(file):
                return Response({"image format is not valid"}, status=status.HTTP_400_BAD_REQUEST)
            
            file = resize_image(file, 800) 
            data['file'] = file
    data['revendeur'] = request.user.userext.revendeur.id
    serializer = TransportSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# TODO Update transport
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_transport(request):
    """
    id -- int (required)
    category -- int (optionnal)
    montant -- float (required)
    date -- date (required)
    proof -- file (optionnal)
    """
    data = request.data.copy()
    file = request.FILES.get('proof')
    transport = get_object_or_404(Transport, pk=request.data['id'])
    if file:
        if not is_image_extension_valid(file):
            return Response({"image format is not valid"}, status=status.HTTP_400_BAD_REQUEST)
        
        # TODO Delete the file exist to replace it with the new one
        transport.proof.delete()
        file = resize_image(file, 800) 
        data['file'] = file
    data['revendeur'] = request.user.userext.revendeur.id
    serializer = TransportSerializer(transport, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete transport
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_transport(request):
    """
    id -- id (required)
    """
    transport = get_object_or_404(Transport, pk=request.data.get('id', None))
    transport.proof.delete()
    transport.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_transport(request):
    personnel = Transport.objects.filter(revendeur=request.user.userext.revendeur.id)
    serializer = TransportSerializer(personnel, many=True)
    return Response(serializer.data)


# ? ================= CATEGORY DIVERS ==================== #

# TODO Create category
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_category(request):
    """
    name -- str (required, max_length=255)
    """
    data = request.data.copy()
    data['revendeur'] = request.user.userext.revendeur.id
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# TODO Update category
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_category(request):
    """
    id -- id (required)
    name -- str (required, max_length=255)
    """
    data = request.data.copy()
    data['revendeur'] = request.user.userext.revendeur.id
    category = get_object_or_404(Category, pk=data['id'])
    serializer = CategorySerializer(category, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete category
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_category(request):
    """
    id -- id (required)
    """
    category = get_object_or_404(Category, pk=request.data.get('id', None))
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_category(request):
    category = Category.objects.filter(revendeur=request.user.userext.revendeur.id).values()
    return Response(category)

# ? ================= DIVERS ==================== #

# TODO Create divers
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_divers(request):
    """
    category -- int (required)
    montant -- float (required)
    date -- date (required)
    proof -- file (optionnal)
    """
    data = request.data.copy()
    file = request.FILES.get('proof')
    if file:
            if not is_image_extension_valid(file):
                return Response({"image format is not valid"}, status=status.HTTP_400_BAD_REQUEST)
            
            file = resize_image(file, 800) 
            data['file'] = file
    serializer = DiversSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# TODO Update divers
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_divers(request):
    """
    id -- int (required)
    category -- int (required)
    montant -- float (required)
    date -- date (required)
    proof -- file (optionnal)
    """
    data = request.data.copy()
    file = request.FILES.get('proof')
    divers = get_object_or_404(Divers, pk=request.data['id'])
    if file:
        if not is_image_extension_valid(file):
            return Response({"image format is not valid"}, status=status.HTTP_400_BAD_REQUEST)
        
        # TODO Delete the file exist to replace it with the new one
        divers.proof.delete()
        file = resize_image(file, 800) 
        data['file'] = file
    serializer = DiversSerializer(divers, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# TODO Delete divers
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_divers(request):
    """
    id -- id (required)
    """
    divers = get_object_or_404(Divers, pk=request.data.get('id', None))
    divers.proof.delete()
    divers.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_divers(request):
    personnel = Divers.objects.filter(category__revendeur=request.user.userext.revendeur.id)
    serializer = DiversSerializer(personnel, many=True)
    return Response(serializer.data)