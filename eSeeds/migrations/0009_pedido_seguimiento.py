# Generated by Django 4.1.3 on 2022-12-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSeeds', '0008_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='seguimiento',
            field=models.IntegerField(choices=[[0, 'Procesando'], [1, 'En envío'], [2, 'Entregado']], null=True),
        ),
    ]
