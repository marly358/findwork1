from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Notificacion
from .serializers import NotificacionSerializer


@api_view(['GET', 'POST'])
def notificaciones(request):

    # GET - listar todas
    if request.method == 'GET':
        notificaciones = Notificacion.objects.all()
        serializer = NotificacionSerializer(notificaciones, many=True)

        return Response(serializer.data)

    # POST - crear
    if request.method == 'POST':
        serializer = NotificacionSerializer(data=request.data)

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


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def notificacion_detalle(request, id):

    try:
        notificacion = Notificacion.objects.get(id=id)
    except Notificacion.DoesNotExist:
        return Response(
            {'error': 'Notificación no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    # GET - obtener una
    if request.method == 'GET':
        serializer = NotificacionSerializer(notificacion)
        return Response(serializer.data)

    # PUT - actualizar completa
    if request.method == 'PUT':
        serializer = NotificacionSerializer(
            notificacion,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # PATCH - actualizar parcialmente
    if request.method == 'PATCH':
        serializer = NotificacionSerializer(
            notificacion,
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

    # DELETE - eliminar
    if request.method == 'DELETE':
        notificacion.delete()

        return Response(
            {'mensaje': 'Notificación eliminada correctamente'},
            status=status.HTTP_204_NO_CONTENT
        )