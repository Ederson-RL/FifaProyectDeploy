# Generated by Django 4.2.7 on 2023-11-25 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_player_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TecnicoNacionality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de la Nacionalidad')),
            ],
            options={
                'verbose_name': 'Nacionalidad',
                'verbose_name_plural': 'Nacionalidades',
            },
        ),
        migrations.CreateModel(
            name='TecnicoRol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name': 'Jugador', 'verbose_name_plural': 'Jugadores'},
        ),
        migrations.AlterModelOptions(
            name='tecnico',
            options={'ordering': ['-id'], 'verbose_name': 'Tecnico', 'verbose_name_plural': 'Tecnicos'},
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='nacionalidad',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tecniconacionality', verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='rol',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tecnicorol', verbose_name='Rol'),
        ),
    ]
