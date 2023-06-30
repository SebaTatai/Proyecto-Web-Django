# Generated by Django 4.1.5 on 2023-06-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_alter_producto_codigo_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(db_column='rutUsuario', max_length=11, primary_key=True, serialize=False),
        ),
    ]
