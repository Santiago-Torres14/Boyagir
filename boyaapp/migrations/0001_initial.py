# Generated by Django 3.1.7 on 2021-03-23 16:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Boya', models.CharField(max_length=50)),
                ('Latitud', models.CharField(max_length=50)),
                ('Longitud', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_Sensor', models.CharField(max_length=10)),
                ('Codigo_Sensor', models.IntegerField(verbose_name=10)),
                ('Voltaje', models.IntegerField()),
                ('Referencia', models.TextField(verbose_name=10)),
                ('Boya', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boyaapp.boya')),
            ],
        ),
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Medicion', django.contrib.postgres.fields.jsonb.JSONField()),
                ('Fecha', models.DateTimeField(auto_now_add=True)),
                ('Boya', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boyaapp.boya')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.TextField(verbose_name=200)),
                ('Medicion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boyaapp.medicion')),
            ],
        ),
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nivel', models.CharField(max_length=100)),
                ('Descripcion', models.TextField(verbose_name=200)),
                ('Evento', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boyaapp.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Afluente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo_Afluente', models.IntegerField(verbose_name=10)),
                ('Nombre_Afluente', models.CharField(max_length=100)),
                ('Nombre_de_departamento', models.CharField(max_length=100)),
                ('Nombre_de_municipio', models.CharField(max_length=100)),
                ('Boya', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boyaapp.boya')),
            ],
        ),
    ]
