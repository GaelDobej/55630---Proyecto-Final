# Generated by Django 4.2.4 on 2023-09-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salute_dArtist', '0004_alter_actor_options_alter_animador_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='nacionalidad',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='animador',
            name='nacionalidad',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='cineasta',
            name='nacionalidad',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='escritor',
            name='nacionalidad',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='escultor',
            name='nacionalidad',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='fotografo',
            name='nacionalidad',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='grabador',
            name='nacionalidad',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='ilustrador',
            name='nacionalidad',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='musico',
            name='nacionalidad',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='pintor',
            name='nacionalidad',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
