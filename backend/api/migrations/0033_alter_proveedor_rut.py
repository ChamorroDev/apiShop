# Generated by Django 4.2.5 on 2023-10-28 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_remove_comprasproveedor_destino_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='rut',
            field=models.IntegerField(null=True),
        ),
    ]
