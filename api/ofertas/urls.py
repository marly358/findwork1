from django.urls import path

from .views import (
    listar_ofertas,
    obtener_oferta,
    crear_oferta,
    actualizar_oferta,
    modificar_oferta,
    eliminar_oferta
)


urlpatterns = [

    # GET y POST
    path('', listar_ofertas),
    path('crear/', crear_oferta),

    # GET por ID
    path('<int:id>/', obtener_oferta),

    # PUT
    path('<int:id>/actualizar/', actualizar_oferta),

    # PATCH
    path('<int:id>/modificar/', modificar_oferta),

    # DELETE
    path('<int:id>/eliminar/', eliminar_oferta),
]