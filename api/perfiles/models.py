from django.db import models


class Candidato(models.Model):
    id = models.IntegerField(primary_key=True)
    carrera = models.CharField(max_length=100, null=True, blank=True)
    semestre = models.IntegerField(null=True, blank=True)
    habilidades = models.TextField(null=True, blank=True)
    universidad = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'candidato'
        managed = False