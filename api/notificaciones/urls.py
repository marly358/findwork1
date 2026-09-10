from django.urls import path

from .views import notificaciones, notificacion_detalle


urlpatterns = [
    path('', notificaciones, name='notificaciones'),
    path('<int:id>/', notificacion_detalle, name='notificacion-detalle'),
]