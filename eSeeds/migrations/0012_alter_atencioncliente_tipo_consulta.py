# Generated by Django 4.1.3 on 2022-12-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSeeds', '0011_remove_pedido_id_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencioncliente',
            name='tipo_consulta',
            field=models.IntegerField(choices=[[0, 'Consulta'], [1, 'Reclamo'], [2, 'Sugerencia'], [3, 'Felicitaciones']]),
        ),
    ]
