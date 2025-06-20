# Generated by Django 5.2.1 on 2025-05-28 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSocial', '0003_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('ubicacion', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cita_usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='appSocial.cita')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='citas', to='appSocial.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField()),
                ('comentario', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reseñas_escritas', to='appSocial.usuario')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reseñas_recibidas', to='appSocial.usuario')),
            ],
        ),
    ]
