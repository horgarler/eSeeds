# Generated by Django 4.1.3 on 2022-12-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSeeds', '0009_pedido_seguimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='id_pedido',
            field=models.TextField(null=True),
        ),
    ]
