# Generated by Django 2.2 on 2020-12-17 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201217_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='added_by',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 19, 48, 10, 843314)),
        ),
    ]
