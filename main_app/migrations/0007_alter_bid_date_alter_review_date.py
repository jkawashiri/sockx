# Generated by Django 4.2.5 on 2023-09-18 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_review_date_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 18, 21, 50, 32, 997139, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 18, 21, 50, 32, 996490, tzinfo=datetime.timezone.utc)),
        ),
    ]
