# Generated by Django 4.1.2 on 2023-05-31 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
