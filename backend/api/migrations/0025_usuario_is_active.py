# Generated by Django 4.2.5 on 2023-10-20 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_bodega_ciudad_bodega_numeracion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
