from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import OfertaLaboral
from .serializers import OfertaLaboralSerializer


# GET - Listar todas las ofertas
@api_view(['GET'])
def listar_ofertas(request):

    ofertas = OfertaLaboral.objects.all()

    serializer = OfertaLaboralSerializer(ofertas, many=True)

    return Response(serializer.data)


# GET - Obtener una oferta por ID
@api_view(['GET'])
def obtener_oferta(request, id):

    try:
        oferta = OfertaLaboral.objects.get(id=id)
    except OfertaLaboral.DoesNotExist:
        return Response(
            {'error': 'Oferta no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = OfertaLaboralSerializer(oferta)

    return Response(serializer.data)


# POST - Crear una oferta
@api_view(['POST'])
def crear_oferta(request):

    serializer = OfertaLaboralSerializer(data=request.data)

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


# PUT - Actualizar completamente una oferta
@api_view(['PUT'])
def actualizar_oferta(request, id):

    try:
        oferta = OfertaLaboral.objects.get(id=id)
    except OfertaLaboral.DoesNotExist:
        return Response(
            {'error': 'Oferta no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = OfertaLaboralSerializer(
        oferta,
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


# PATCH - Actualizar parcialmente una oferta
@api_view(['PATCH'])
def modificar_oferta(request, id):

    try:
        oferta = OfertaLaboral.objects.get(id=id)
    except OfertaLaboral.DoesNotExist:
        return Response(
            {'error': 'Oferta no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = OfertaLaboralSerializer(
        oferta,
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


# DELETE - Eliminar una oferta
@api_view(['DELETE'])
def eliminar_oferta(request, id):

    try:
        oferta = OfertaLaboral.objects.get(id=id)
    except OfertaLaboral.DoesNotExist:
        return Response(
            {'error': 'Oferta no encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )

    oferta.delete()

    return Response(
        {'mensaje': 'Oferta eliminada correctamente'},
        status=status.HTTP_204_NO_CONTENT
    )