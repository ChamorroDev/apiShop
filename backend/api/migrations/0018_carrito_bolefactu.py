# Generated by Django 4.2.5 on 2023-10-06 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_retiropersona_carrito_direccion_carrito_sucursal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='bolefactu',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
