# Generated by Django 2.1.5 on 2022-05-21 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='Date',
            new_name='fecha',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='time',
            new_name='hora',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='number_of_persons',
            new_name='numero_de_personas',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='phone',
            new_name='numero_de_telefono',
        ),
    ]
