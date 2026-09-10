from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuarios, name='usuarios'),
    path('<int:id>/', views.usuario_detalle, name='usuario_detalle'),
]