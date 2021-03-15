# Generated by Django 3.1.7 on 2021-03-12 20:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0021_auto_20210312_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.profile'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='screening_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 12, 20, 57, 50, 228263, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 12, 20, 57, 50, 227257, tzinfo=utc)),
        ),
    ]