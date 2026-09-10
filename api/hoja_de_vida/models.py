from django.db import models


class HojaDeVida(models.Model):
    id = models.AutoField(primary_key=True)

    urlArchivo = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    fechaCarga = models.DateField(
        null=True,
        blank=True
    )

    tamanoMB = models.FloatField(
        null=True,
        blank=True
    )

    candidato = models.OneToOneField(
        'perfiles.Candidato',
        on_delete=models.CASCADE,
        db_column='candidato_id',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'hojadevida'
        managed = False

    def __str__(self):
        return f"Hoja de vida {self.id}"