# Generated by Django 4.1.3 on 2022-12-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSeeds', '0006_rename_fechanacimiento_cliente_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='atencionCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencia'], [3, 'felicitaciones']])),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
