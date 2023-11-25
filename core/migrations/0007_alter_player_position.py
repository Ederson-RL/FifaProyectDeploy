# Generated by Django 4.2.7 on 2023-11-25 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_tecnico_nacionalidad_alter_tecnico_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.playingposition', verbose_name='Posicion en la que juega'),
        ),
    ]