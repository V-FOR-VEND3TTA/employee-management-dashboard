# Generated by Django 3.2.20 on 2023-08-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20230820_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=40),
        ),
    ]
