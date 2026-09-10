from django.db import models


class Postulacion(models.Model):
    id = models.AutoField(primary_key=True)
    fechaPostulacion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)
    candidato_id = models.IntegerField(null=True, blank=True)
    oferta_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'postulacion'
        managed = False