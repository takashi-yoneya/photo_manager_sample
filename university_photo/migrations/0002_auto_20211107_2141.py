# Generated by Django 3.2.9 on 2021-11-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university_photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumaster',
            name='finish_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='menumaster',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
