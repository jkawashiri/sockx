# Generated by Django 4.2.5 on 2023-09-20 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_shoe_shoe_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='shoe_photo',
        ),
    ]
