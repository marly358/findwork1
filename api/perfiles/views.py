from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Candidato
from .serializers import CandidatoSerializer


# GET - Listar todos los perfiles
@api_view(['GET'])
def listar_perfiles(request):

    candidatos = Candidato.objects.all()

    serializer = CandidatoSerializer(candidatos, many=True)

    return Response(serializer.data)


# GET - Obtener un perfil por ID
@api_view(['GET'])
def obtener_perfil(request, id):

    try:
        candidato = Candidato.objects.get(id=id)
    except Candidato.DoesNotExist:
        return Response(
            {'error': 'Perfil no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CandidatoSerializer(candidato)

    return Response(serializer.data)


# POST - Crear un perfil
@api_view(['POST'])
def crear_perfil(request):

    serializer = CandidatoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


# PUT - Actualizar completamente un perfil
@api_view(['PUT'])
def actualizar_perfil(request, id):

    try:
        candidato = Candidato.objects.get(id=id)
    except Candidato.DoesNotExist:
        return Response(
            {'error': 'Perfil no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CandidatoSerializer(
        candidato,
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


# PATCH - Actualizar parcialmente un perfil
@api_view(['PATCH'])
def modificar_perfil(request, id):

    try:
        candidato = Candidato.objects.get(id=id)
    except Candidato.DoesNotExist:
        return Response(
            {'error': 'Perfil no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CandidatoSerializer(
        candidato,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


# DELETE - Eliminar un perfil
@api_view(['DELETE'])
def eliminar_perfil(request, id):

    try:
        candidato = Candidato.objects.get(id=id)
    except Candidato.DoesNotExist:
        return Response(
            {'error': 'Perfil no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    candidato.delete()

    return Response(
        {'mensaje': 'Perfil eliminado correctamente'},
        status=status.HTTP_204_NO_CONTENT
    )