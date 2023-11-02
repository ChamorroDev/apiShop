# Generated by Django 4.2.5 on 2023-10-31 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_alter_proveedor_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprasproveedor',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.estadopedido'),
        ),
        migrations.AddField(
            model_name='comprasproveedor',
            name='obs',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
