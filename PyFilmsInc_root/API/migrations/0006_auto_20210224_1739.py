# Generated by Django 3.1.7 on 2021-02-24 17:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20210224_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='screening_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 17, 39, 41, 231405, tzinfo=utc)),
        ),
    ]
