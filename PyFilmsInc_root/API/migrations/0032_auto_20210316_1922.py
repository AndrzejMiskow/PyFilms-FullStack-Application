# Generated by Django 3.1.7 on 2021-03-16 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0031_auto_20210316_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='lead_booking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='API.reservation'),
        ),
    ]
