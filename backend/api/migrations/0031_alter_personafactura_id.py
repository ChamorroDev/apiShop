# Generated by Django 4.2.5 on 2023-10-23 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_carrito_razonfactura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personafactura',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]