# Generated by Django 3.2 on 2021-12-22 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerias', '0002_cuadro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadro',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]
