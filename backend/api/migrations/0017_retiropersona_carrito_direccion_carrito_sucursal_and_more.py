# Generated by Django 4.2.5 on 2023-10-06 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_boleta_sucursal_factura_sucursal'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetiroPersona',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='carrito',
            name='direccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.direccion'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='sucursal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.sucursal'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='tipoDespacho',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.tipodespacho'),
        ),
        migrations.CreateModel(
            name='personaFactura',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('rut', models.IntegerField()),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='boleta',
            name='retiroPersona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.retiropersona'),
        ),
        migrations.AddField(
            model_name='carrito',
            name='retiroPersona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.retiropersona'),
        ),
        migrations.AddField(
            model_name='factura',
            name='personaFactura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.personafactura'),
        ),
        migrations.AddField(
            model_name='factura',
            name='retiroPersona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.retiropersona'),
        ),
    ]