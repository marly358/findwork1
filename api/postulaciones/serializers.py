from rest_framework import serializers
from .models import Postulacion


class PostulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulacion
        fields = [
            'id',
            'fechaPostulacion',
            'estado',
            'candidato_id',
            'oferta_id'
        ]