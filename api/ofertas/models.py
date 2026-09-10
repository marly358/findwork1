from django.db import models


class OfertaLaboral(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    salario = models.FloatField(null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=30, null=True, blank=True)
    modalidad = models.CharField(max_length=20, null=True, blank=True)
    aprobada = models.BooleanField(null=True, blank=True)
    fechaPublicacion = models.DateField(null=True, blank=True)
    empleador_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'ofertalaboral'
        managed = False