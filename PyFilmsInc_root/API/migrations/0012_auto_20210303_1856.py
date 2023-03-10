# Generated by Django 3.1.7 on 2021-03-03 18:56

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0011_auto_20210226_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('CARD', 'Card Payment'), ('CASH', 'Cash Payment')], default='CARD', max_length=32)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2021, 3, 3, 18, 56, 42, 329585, tzinfo=utc))),
                ('amount', models.FloatField()),
                ('successful', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=32)),
                ('password', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(8)])),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_type_id',
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_type',
            field=models.CharField(choices=[('ADULT', 'Adult'), ('CHILD', 'Child'), ('SENIOR', 'Senior'), ('STUDENT', 'Student')], default='ADULT', max_length=32),
        ),
        migrations.AddField(
            model_name='screening',
            name='movie_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.movie'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='screening_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 18, 56, 42, 447208, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='ReservationType',
        ),
        migrations.AddField(
            model_name='transaction',
            name='used_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.user'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='API.user'),
        ),
    ]
