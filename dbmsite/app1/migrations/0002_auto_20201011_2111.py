# Generated by Django 3.1.2 on 2020-10-11 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='proname',
            new_name='pn',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='studentname',
            new_name='sn',
        ),
    ]