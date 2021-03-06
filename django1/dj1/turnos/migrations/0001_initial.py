# Generated by Django 3.0.8 on 2020-09-05 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuit', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=30)),
                ('descrpcion', models.CharField(max_length=30)),
                ('rubro', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.IntegerField()),
                ('fecha', models.CharField(max_length=30)),
                ('hora', models.CharField(max_length=30)),
                ('idcliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turnos.Cliente')),
                ('idproveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turnos.Proveedor')),
            ],
        ),
    ]
