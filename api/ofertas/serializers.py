from rest_framework import serializers
from .models import OfertaLaboral


class OfertaLaboralSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfertaLaboral
        fields = [
            'id',
            'titulo',
            'descripcion',
            'salario',
            'ciudad',
            'area',
            'modalidad',
            'aprobada',
            'fechaPublicacion',
            'empleador_id'
        ]