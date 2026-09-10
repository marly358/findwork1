from django.db import models


class RolUsuario(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True)

    class Meta:
        db_table = 'rolusuario'


class AreaProfesional(models.Model):
    nombre = models.CharField(max_length=30, primary_key=True)

    class Meta:
        db_table = 'areaprofesional'


class ModalidadTrabajo(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True)

    class Meta:
        db_table = 'modalidadtrabajo'


class EstadoPostulacion(models.Model):
    nombre = models.CharField(max_length=20, primary_key=True)

    class Meta:
        db_table = 'estadopostulacion'


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    passwordHash = models.CharField(max_length=255, null=True, blank=True)
    rol = models.ForeignKey(
        RolUsuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='rol'
    )
    activo = models.BooleanField(null=True, blank=True)
    fechaRegistro = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'usuario'


class Empleador(models.Model):
    id = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='id'
    )
    empresa = models.CharField(max_length=100, null=True, blank=True)
    nit = models.CharField(max_length=50, null=True, blank=True)
    emailCorporativo = models.EmailField(max_length=100, null=True, blank=True)
    verificado = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = 'empleador'


class Candidato(models.Model):
    id = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='id'
    )
    carrera = models.CharField(max_length=100, null=True, blank=True)
    semestre = models.IntegerField(null=True, blank=True)
    habilidades = models.TextField(null=True, blank=True)
    universidad = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'candidato'


class Administrador(models.Model):
    id = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        primary_key=True,
        db_column='id'
    )
    nivelAcceso = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'administrador'


class HojaDeVida(models.Model):
    id = models.AutoField(primary_key=True)
    urlArchivo = models.CharField(max_length=255, null=True, blank=True)
    fechaCarga = models.DateField(null=True, blank=True)
    tamanoMB = models.FloatField(null=True, blank=True)
    candidato = models.OneToOneField(
        Candidato,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='candidato_id'
    )

    class Meta:
        db_table = 'hojadevida'


class Notificacion(models.Model):
    id = models.AutoField(primary_key=True)
    destinatario = models.CharField(max_length=100, null=True, blank=True)
    mensaje = models.TextField(null=True, blank=True)
    fechaEnvio = models.DateField(null=True, blank=True)
    enviada = models.BooleanField(null=True, blank=True)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='usuario_id'
    )

    class Meta:
        db_table = 'notificacion'


class OfertaLaboral(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    salario = models.FloatField(null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    area = models.ForeignKey(
        AreaProfesional,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='area'
    )
    modalidad = models.ForeignKey(
        ModalidadTrabajo,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='modalidad'
    )
    aprobada = models.BooleanField(null=True, blank=True)
    fechaPublicacion = models.DateField(null=True, blank=True)
    empleador = models.ForeignKey(
        Empleador,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='empleador_id'
    )

    class Meta:
        db_table = 'ofertalaboral'


class Postulacion(models.Model):
    id = models.AutoField(primary_key=True)
    fechaPostulacion = models.DateField(null=True, blank=True)
    estado = models.ForeignKey(
        EstadoPostulacion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='estado'
    )
    candidato = models.ForeignKey(
        Candidato,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='candidato_id'
    )
    oferta = models.ForeignKey(
        OfertaLaboral,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='oferta_id'
    )

    class Meta:
        db_table = 'postulacion'



