# Generated by Django 4.1.2 on 2023-07-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0005_alter_producto_codigo_producto_carrito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='codigo_carrito',
            field=models.IntegerField(db_column='codigoCarrito', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='codigo_categoria',
            field=models.IntegerField(db_column='codigoCategoria', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo_producto',
            field=models.IntegerField(db_column='codigoProducto', primary_key=True, serialize=False),
        ),
    ]