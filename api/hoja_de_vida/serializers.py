from rest_framework import serializers
from .models import HojaDeVida


class HojaDeVidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HojaDeVida
        fields = [
            'id',
            'urlArchivo',
            'fechaCarga',
            'tamanoMB',
            'candidato'
        ]