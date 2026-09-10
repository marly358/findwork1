from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'destinatario',
                    models.CharField(db_column='destinario', max_length=255),
                ),
                ('mensaje', models.TextField()),
                ('fechaEnvio', models.DateTimeField(auto_now_add=True)),
                ('enviada', models.BooleanField(default=False)),
                ('usuario_id', models.IntegerField()),
            ],
            options={
                'db_table': 'notificacion',
                'managed': False,
                'ordering': ['-fechaEnvio'],
            },
        ),
    ]
