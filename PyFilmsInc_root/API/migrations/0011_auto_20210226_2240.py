# Generated by Django 3.1.7 on 2021-02-26 22:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0010_auto_20210226_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='screening_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 26, 22, 40, 48, 636421, tzinfo=utc)),
        ),
    ]
