# Generated by Django 5.0.7 on 2024-08-04 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0003_alter_parcel_order_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='open_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='open datetime'),
        ),
        migrations.AlterField(
            model_name='parcel',
            name='update_datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='update datetime'),
        ),
    ]