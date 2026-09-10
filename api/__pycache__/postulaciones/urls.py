from django.urls import path

from .views import (
    listar_postulaciones,
    obtener_postulacion,
    crear_postulacion,
    actualizar_postulacion,
    modificar_postulacion,
    eliminar_postulacion
)


urlpatterns = [

    # GET - listar
    path('', listar_postulaciones),

    # POST - crear
    path('crear/', crear_postulacion),

    # GET - obtener por ID
    path('<int:id>/', obtener_postulacion),

    # PUT
    path('<int:id>/actualizar/', actualizar_postulacion),

    # PATCH
    path('<int:id>/modificar/', modificar_postulacion),

    # DELETE
    path('<int:id>/eliminar/', eliminar_postulacion),
]