# Generated by Django 3.2.20 on 2023-08-22 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20230822_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='clocked_in',
            field=models.TimeField(default='08:00', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='time_authorized',
            field=models.TimeField(blank=True, default='08:00', null=True),
        ),
    ]
