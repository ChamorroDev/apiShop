# Generated by Django 4.2.5 on 2023-10-20 22:27

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_usuario_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(null=True, upload_to=api.models.cargar_foto),
        ),
    ]
