# Generated by Django 3.2.20 on 2023-08-20 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_employee_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
    ]