# Generated by Django 4.2.4 on 2023-09-03 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Salute_dArtist', '0009_rename_musicoservice_serviciomusical'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServicioMusical',
            new_name='ServicioMusicalModel',
        ),
    ]