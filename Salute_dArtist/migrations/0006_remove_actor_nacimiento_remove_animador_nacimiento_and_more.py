# Generated by Django 4.2.4 on 2023-09-03 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Salute_dArtist', '0005_actor_nacionalidad_animador_nacionalidad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='animador',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='cineasta',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='escritor',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='escultor',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='fotografo',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='grabador',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='ilustrador',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='musico',
            name='nacimiento',
        ),
        migrations.RemoveField(
            model_name='pintor',
            name='nacimiento',
        ),
    ]