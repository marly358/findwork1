from django.urls import path

from .views import (
    listar_perfiles,
    obtener_perfil,
    crear_perfil,
    actualizar_perfil,
    modificar_perfil,
    eliminar_perfil
)


urlpatterns = [

    path('', listar_perfiles),

    path('crear/', crear_perfil),

    path('<int:id>/', obtener_perfil),

    path('<int:id>/actualizar/', actualizar_perfil),

    path('<int:id>/modificar/', modificar_perfil),

    path('<int:id>/eliminar/', eliminar_perfil),
]