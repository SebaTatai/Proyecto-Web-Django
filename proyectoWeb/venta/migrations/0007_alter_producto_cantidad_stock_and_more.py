# Generated by Django 4.1.2 on 2023-07-07 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0006_alter_carrito_codigo_carrito_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad_stock',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo_producto',
            field=models.CharField(db_column='codigoProducto', max_length=25, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.CharField(max_length=25),
        ),
    ]