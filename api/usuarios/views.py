from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario


@api_view(['GET', 'POST'])
def usuarios(request):

    # =========================
    # GET - LISTAR USUARIOS
    # =========================
    if request.method == 'GET':
        usuarios = Usuario.objects.all()

        datos = []

        for usuario in usuarios:
            datos.append({
                'id': usuario.id,
                'nombre': usuario.nombre,
                'email': usuario.email,
                'rol': usuario.rol_id,
                'activo': usuario.activo,
                'fechaRegistro': usuario.fechaRegistro
            })

        return Response(datos)

   
    if request.method == 'POST':

        usuario = Usuario.objects.create(
            nombre=request.data.get('nombre'),
            email=request.data.get('email'),
            passwordHash=request.data.get('passwordHash'),
            rol_id=request.data.get('rol'),
            activo=request.data.get('activo', True),
            fechaRegistro=request.data.get('fechaRegistro')
        )

        return Response({
            'mensaje': 'Usuario creado correctamente',
            'usuario': {
                'id': usuario.id,
                'nombre': usuario.nombre,
                'email': usuario.email,
                'rol': usuario.rol_id,
                'activo': usuario.activo,
                'fechaRegistro': usuario.fechaRegistro
            }
        }, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PATCH', 'DELETE'])
def usuario_detalle(request, id):

    # Buscar usuario
    try:
        usuario = Usuario.objects.get(id=id)
    except Usuario.DoesNotExist:
        return Response(
            {'error': 'Usuario no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )



    if request.method == 'GET':

        return Response({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'email': usuario.email,
            'rol': usuario.rol_id,
            'activo': usuario.activo,
            'fechaRegistro': usuario.fechaRegistro
        })

   
    if request.method == 'PATCH':

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

    if request.method == 'DELETE':

        usuario.delete()

        return Response(
            {'mensaje': 'Usuario eliminado correctamente'},
            status=status.HTTP_204_NO_CONTENT
        )