# Generated by Django 4.2.5 on 2023-09-18 22:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0008_bid_user_alter_bid_date_alter_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 18, 22, 28, 26, 362200, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 18, 22, 28, 26, 361405, tzinfo=datetime.timezone.utc)),
        ),
    ]
