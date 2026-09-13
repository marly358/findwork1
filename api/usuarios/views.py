from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario
from .serializers import UsuarioSerializer


@api_view(['GET', 'POST'])
def usuarios(request):

    # =========================
    # GET - LISTAR USUARIOS
    # =========================
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    # =========================
    # POST - CREAR USUARIO
    # =========================
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def usuario_detalle(request, id):

    # Buscar usuario
    try:
        usuario = Usuario.objects.get(id=id)
    except Usuario.DoesNotExist:
        return Response(
            {'error': 'Usuario no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    # =========================
    # GET - CONSULTAR USUARIO
    # =========================
    if request.method == 'GET':

        return Response({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'email': usuario.email,
            'rol': usuario.rol_id,
            'activo': usuario.activo,
            'fechaRegistro': usuario.fechaRegistro
        })

    # =========================
    # PUT/PATCH - ACTUALIZAR USUARIO
    # =========================
    if request.method in ('PUT', 'PATCH'):

        if request.method == 'PUT':
            campos_requeridos = ('nombre', 'email', 'passwordHash', 'rol', 'activo', 'fechaRegistro')
            campos_faltantes = [campo for campo in campos_requeridos if campo not in request.data]

            if campos_faltantes:
                return Response(
                    {'error': 'Faltan campos requeridos', 'campos': campos_faltantes},
                    status=status.HTTP_400_BAD_REQUEST
                )

        if 'nombre' in request.data:
            usuario.nombre = request.data['nombre']

        if 'email' in request.data:
            usuario.email = request.data['email']

        if 'passwordHash' in request.data:
            usuario.passwordHash = request.data['passwordHash']

        if 'rol' in request.data:
            usuario.rol_id = request.data['rol']

        if 'activo' in request.data:
            usuario.activo = request.data['activo']

        if 'fechaRegistro' in request.data:
            usuario.fechaRegistro = request.data['fechaRegistro']

        usuario.save()

        return Response({
            'mensaje': 'Usuario actualizado correctamente',
            'usuario': {
                'id': usuario.id,
                'nombre': usuario.nombre,
                'email': usuario.email,
                'rol': usuario.rol_id,
                'activo': usuario.activo,
                'fechaRegistro': usuario.fechaRegistro
            }
        })

    # =========================
    # DELETE - ELIMINAR USUARIO
    # =========================
    if request.method == 'DELETE':

        usuario.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)