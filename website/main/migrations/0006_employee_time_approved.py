# Generated by Django 3.2.20 on 2023-08-18 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20230818_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='time_approved',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
