# Generated by Django 3.0.6 on 2020-05-21 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wpis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=100)),
                ('tresc', models.CharField(max_length=140)),
                ('gram', models.IntegerField()),
            ],
        ),
    ]
