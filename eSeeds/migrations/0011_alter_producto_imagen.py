# Generated by Django 4.1.3 on 2022-12-11 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSeeds', '0010_pedido_id_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
