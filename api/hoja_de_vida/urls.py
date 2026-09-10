from django.urls import path

from .views import hojas_de_vida, hoja_de_vida_detalle


urlpatterns = [
    path('', hojas_de_vida, name='hojas-de-vida'),
    path('<int:id>/', hoja_de_vida_detalle, name='hoja-de-vida-detalle'),
]