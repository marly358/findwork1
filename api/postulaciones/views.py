from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Postulacion
from .serializers import PostulacionSerializer


# GET - Listar todas las postulaciones
@api_view(['GET'])
def listar_postulaciones(request):

    postulaciones = Postulacion.objects.all()

    serializer = PostulacionSerializer(
        postulaciones,
        many=True
    )

    return Response(serializer.data)


# GET - Obtener una postulación por ID
@api_view(['GET'])
def obtener_postulacion(request, id):

    try:
        postulacion = Postulacion.objects.get(id=id)

    except Postulacion.DoesNotExist:
        return Response(
            {'error': 'Postulación no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = PostulacionSerializer(postulacion)

    return Response(serializer.data)


# POST - Crear una postulación
@api_view(['POST'])
def crear_postulacion(request):

    serializer = PostulacionSerializer(data=request.data)

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


# PUT - Actualizar completamente una postulación
@api_view(['PUT'])
def actualizar_postulacion(request, id):

    try:
        postulacion = Postulacion.objects.get(id=id)

    except Postulacion.DoesNotExist:
        return Response(
            {'error': 'Postulación no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = PostulacionSerializer(
        postulacion,
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


# PATCH - Actualizar parcialmente una postulación
@api_view(['PATCH'])
def modificar_postulacion(request, id):

    try:
        postulacion = Postulacion.objects.get(id=id)

    except Postulacion.DoesNotExist:
        return Response(
            {'error': 'Postulación no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = PostulacionSerializer(
        postulacion,
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


# DELETE - Eliminar una postulación
@api_view(['DELETE'])
def eliminar_postulacion(request, id):

    try:
        postulacion = Postulacion.objects.get(id=id)

    except Postulacion.DoesNotExist:
        return Response(
            {'error': 'Postulación no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    postulacion.delete()

    return Response(
        {'mensaje': 'Postulación eliminada correctamente'},
        status=status.HTTP_204_NO_CONTENT
    )