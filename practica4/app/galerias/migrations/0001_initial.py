# Generated by Django 3.2 on 2021-12-13 20:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cuadro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('autor', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField(default=django.utils.timezone.now)),
                ('galeria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galerias.galeria')),
            ],
        ),
    ]
