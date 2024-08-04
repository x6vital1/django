# Generated by Django 5.0.7 on 2024-07-28 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0001_initial'),
        ('post_machine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='locker',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='post_machine.locker'),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='open_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
    ]