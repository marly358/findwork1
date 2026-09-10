from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import HojaDeVida
from .serializers import HojaDeVidaSerializer


@api_view(['GET', 'POST'])
def hojas_de_vida(request):

    # GET - listar todas las hojas de vida
    if request.method == 'GET':
        hojas = HojaDeVida.objects.all()
        serializer = HojaDeVidaSerializer(hojas, many=True)

        return Response(serializer.data)

    # POST - crear hoja de vida
    if request.method == 'POST':
        serializer = HojaDeVidaSerializer(data=request.data)

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
def hoja_de_vida_detalle(request, id):

    try:
        hoja = HojaDeVida.objects.get(id=id)

    except HojaDeVida.DoesNotExist:
        return Response(
            {'error': 'Hoja de vida no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    # GET - obtener una hoja de vida
    if request.method == 'GET':
        serializer = HojaDeVidaSerializer(hoja)

        return Response(serializer.data)

    # PUT - actualizar completamente
    if request.method == 'PUT':
        serializer = HojaDeVidaSerializer(
            hoja,
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
        serializer = HojaDeVidaSerializer(
            hoja,
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
        hoja.delete()

        return Response(
            {'mensaje': 'Hoja de vida eliminada correctamente'},
            status=status.HTTP_204_NO_CONTENT
        )