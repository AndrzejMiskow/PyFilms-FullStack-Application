# Generated by Django 3.1.7 on 2021-03-12 21:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0023_auto_20210312_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='card_number',
            field=models.IntegerField(blank=True, max_length=16, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='exp_date',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='screening',
            name='screening_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 12, 21, 9, 17, 793749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 12, 21, 9, 17, 792475, tzinfo=utc)),
        ),
    ]
