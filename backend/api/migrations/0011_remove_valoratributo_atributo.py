# Generated by Django 4.2.5 on 2023-09-30 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_persona_ciudad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valoratributo',
            name='atributo',
        ),
    ]
