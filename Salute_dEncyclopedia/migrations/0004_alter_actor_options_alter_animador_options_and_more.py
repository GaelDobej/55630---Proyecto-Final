# Generated by Django 4.2.4 on 2023-08-31 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salute_dEncyclopedia', '0003_actor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': 'Actor', 'verbose_name_plural': 'Actores'},
        ),
        migrations.AlterModelOptions(
            name='animador',
            options={'verbose_name': 'Animador', 'verbose_name_plural': 'Animadores'},
        ),
        migrations.AlterModelOptions(
            name='escritor',
            options={'verbose_name': 'Escritor', 'verbose_name_plural': 'Escritores'},
        ),
        migrations.AlterModelOptions(
            name='escultor',
            options={'verbose_name': 'Escultor', 'verbose_name_plural': 'Escultores'},
        ),
        migrations.AlterModelOptions(
            name='grabador',
            options={'verbose_name': 'Grabador', 'verbose_name_plural': 'Grabadores'},
        ),
        migrations.AlterModelOptions(
            name='ilustrador',
            options={'verbose_name': 'Ilustrador', 'verbose_name_plural': 'Ilustradores'},
        ),
        migrations.AlterModelOptions(
            name='pintor',
            options={'verbose_name': 'Pintor', 'verbose_name_plural': 'Pintores'},
        ),
        migrations.AddField(
            model_name='actor',
            name='nacionalidad',
            field=models.CharField(default='Sin nacionalidad especificada', max_length=50),
        ),
        migrations.AddField(
            model_name='animador',
            name='nacionalidad',
            field=models.CharField(default='Sin nacionalidad especificada', max_length=50),
        ),
        migrations.AddField(
            model_name='cineasta',
            name='nacionalidad',
            field=models.CharField(default='Sin nacionalidad especificada', max_length=50),
        ),
        migrations.AddField(
            model_name='escritor',
            name='nacionalidad',
            field=models.CharField(default='Sin nacionalidad especificada', max_length=50),
        ),
        migrations.AddField(
            model_name='escultor',
            name='nacionalidad',
            field=models.CharField(default='Sin nacionalidad especificada', max_length=50),
        ),
        migrations.AddField(
            model_name='fotografo',
            name='nacionalidad',
            field=models.CharField(default='Sin nacionalidad especificada', max_length=50),
        ),
        migrations.AddField(
            model_name='grabador',
            name='nacionalidad',
            field=models.CharField(default='Sin nacionalidad especificada', max_length=50),
        ),
        migrations.AddField(
            model_name='ilustrador',
            name='nacionalidad',
            field=models.CharField(default='Sin nacionalidad especificada', max_length=50),
        ),
        migrations.AddField(
            model_name='musico',
            name='nacionalidad',
            field=models.CharField(default='Sin nacionalidad especificada', max_length=50),
        ),
        migrations.AddField(
            model_name='pintor',
            name='nacionalidad',
            field=models.CharField(default='Sin nacionalidad especificada', max_length=50),
        ),
    ]
