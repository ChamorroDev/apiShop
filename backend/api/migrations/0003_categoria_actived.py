# Generated by Django 4.2.5 on 2023-09-18 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_categoria_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='actived',
            field=models.BooleanField(default=True),
        ),
    ]
