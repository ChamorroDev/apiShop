# Generated by Django 4.2.5 on 2023-09-19 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]
