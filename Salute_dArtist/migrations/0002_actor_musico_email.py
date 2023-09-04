# Generated by Django 4.2.4 on 2023-09-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salute_dArtist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nacimiento', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='musico',
            name='email',
            field=models.EmailField(default='Desconocido', max_length=254),
        ),
    ]