# Generated by Django 4.1.2 on 2022-11-19 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APLICACION', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='fechacitacion',
            field=models.DateField(),
        ),
    ]
