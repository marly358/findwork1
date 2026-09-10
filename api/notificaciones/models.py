from django.db import models


class Notificacion(models.Model):
    id = models.AutoField(primary_key=True)
    destinatario = models.CharField(max_length=100, null=True, blank=True)
    mensaje = models.TextField(null=True, blank=True)
    fechaEnvio = models.DateField(null=True, blank=True)
    enviada = models.BooleanField(null=True, blank=True)

    usuario = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.CASCADE,
        db_column='usuario_id',
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'notificacion'
        managed = False

    def __str__(self):
        return f"Notificación {self.id}"