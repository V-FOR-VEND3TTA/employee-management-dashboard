# Generated by Django 3.2.20 on 2023-08-20 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20230821_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='clocked_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='clocked_out',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='shift_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]