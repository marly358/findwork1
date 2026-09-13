
from django.urls import path

from .views import (
    listar_notificaciones,
    obtener_notificacion,
    crear_notificacion,
    actualizar_notificacion,
    modificar_notificacion,
    eliminar_notificacion
)


urlpatterns = [

    # GET y POST
    path('', listar_notificaciones),
    path('crear/', crear_notificacion),

    # GET por ID
    path('<int:id>/', obtener_notificacion),

    # PUT
    path('<int:id>/actualizar/', actualizar_notificacion),

    # PATCH
    path('<int:id>/modificar/', modificar_notificacion),

    # DELETE
    path('<int:id>/eliminar/', eliminar_notificacion),
]
