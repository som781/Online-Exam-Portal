# Generated by Django 3.1.2 on 2020-10-11 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=200)),
                ('proname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='detials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp', models.CharField(max_length=500)),
                ('ps', models.CharField(max_length=500)),
                ('prostu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.students')),
            ],
        ),
    ]