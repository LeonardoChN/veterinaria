# Generated by Django 4.1.2 on 2022-11-30 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APLICACION', '0008_rename_rut_funcionario_clientes_rut_cliente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cita',
            old_name='tipoat',
            new_name='atencion',
        ),
    ]
