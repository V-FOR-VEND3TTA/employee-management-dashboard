# Generated by Django 3.2.20 on 2023-08-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20230822_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='time_authorized',
            field=models.TimeField(blank=True, default='09:00', null=True),
        ),
    ]
