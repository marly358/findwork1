from django.db import models


class RolUsuario(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True)

    class Meta:
        db_table = 'rolusuario'
        managed = False


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    passwordHash = models.CharField(max_length=255, null=True, blank=True)

    rol = models.ForeignKey(
        RolUsuario,
        on_delete=models.PROTECT,
        db_column='rol',
        null=True,
        blank=True
    )

    activo = models.BooleanField(null=True, blank=True)
    fechaRegistro = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'usuario'
        managed = False