# Generated by Django 3.1.7 on 2021-02-24 16:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API_reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='screening_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 16, 41, 49, 292429, tzinfo=utc)),
        ),
    ]
