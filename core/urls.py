from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('usuarios/', include('api.usuarios.urls')),
    path('perfiles/', include('api.perfiles.urls')),
    path('hoja-de-vida/', include('api.hoja_de_vida.urls')),
    path('ofertas/', include('api.ofertas.urls')),
    path('postulaciones/', include('api.postulaciones.urls')),
    path('notificaciones/', include('api.notificaciones.urls')),
]