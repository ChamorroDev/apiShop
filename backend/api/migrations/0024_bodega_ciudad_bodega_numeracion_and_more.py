# Generated by Django 4.2.5 on 2023-10-19 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_carrito_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodega',
            name='ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ciudad'),
        ),
        migrations.AddField(
            model_name='bodega',
            name='numeracion',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bodega',
            name='direccion',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('actived', models.IntegerField(blank=True, null=True)),
                ('rut', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.persona')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('actived', models.IntegerField(blank=True, null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='ComprasProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.bodega')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.producto')),
            ],
        ),
    ]
