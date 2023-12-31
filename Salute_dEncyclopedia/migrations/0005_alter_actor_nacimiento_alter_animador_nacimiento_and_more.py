# Generated by Django 4.2.4 on 2023-09-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salute_dEncyclopedia', '0004_alter_actor_options_alter_animador_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='nacimiento',
            field=models.DateField(default='Desconocido'),
        ),
        migrations.AlterField(
            model_name='animador',
            name='nacimiento',
            field=models.DateField(default='Desconocido'),
        ),
        migrations.AlterField(
            model_name='cineasta',
            name='nacimiento',
            field=models.DateField(default='Desconocido'),
        ),
        migrations.AlterField(
            model_name='escritor',
            name='nacimiento',
            field=models.DateField(default='Desconocido'),
        ),
        migrations.AlterField(
            model_name='escultor',
            name='nacimiento',
            field=models.DateField(default='Desconocido'),
        ),
        migrations.AlterField(
            model_name='fotografo',
            name='nacimiento',
            field=models.DateField(default='Desconocido'),
        ),
        migrations.AlterField(
            model_name='grabador',
            name='nacimiento',
            field=models.DateField(default='Desconocido'),
        ),
        migrations.AlterField(
            model_name='ilustrador',
            name='nacimiento',
            field=models.DateField(default='Desconocido'),
        ),
        migrations.AlterField(
            model_name='musico',
            name='nacimiento',
            field=models.DateField(default='Desconocido'),
        ),
        migrations.AlterField(
            model_name='pintor',
            name='nacimiento',
            field=models.DateField(default='Desconocido'),
        ),
    ]
