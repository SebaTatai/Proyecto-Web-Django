# Generated by Django 4.1.2 on 2023-05-31 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('codigo_categoria', models.AutoField(db_column='codigoCategoria', primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.AutoField(db_column='rutUsuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido_paterno', models.CharField(max_length=25)),
                ('apellido_materno', models.CharField(max_length=25)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=110, unique=True)),
                ('direccion', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo_producto', models.AutoField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio', models.IntegerField()),
                ('cantidad_stock', models.IntegerField()),
                ('codigo_categoria', models.ForeignKey(db_column='codigoCategoria', on_delete=django.db.models.deletion.CASCADE, to='venta.categoria')),
            ],
        ),
    ]