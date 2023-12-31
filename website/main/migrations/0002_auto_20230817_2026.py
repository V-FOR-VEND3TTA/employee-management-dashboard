# Generated by Django 3.2.20 on 2023-08-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(choices=[('IT', 'IT'), ('Sales', 'Sales'), ('Marketing', 'Marketing'), ('HR', 'Human Resources')], max_length=100, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('shift_date', models.DateField()),
                ('clocked_in', models.DateTimeField()),
                ('clocked_out', models.DateTimeField()),
                ('time_code', models.CharField(choices=[('TC1', 'Time Code 1'), ('TC2', 'Time Code 2')], max_length=20)),
                ('attendance_code', models.CharField(choices=[('AC1', 'Attendance Code 1'), ('AC2', 'Attendance Code 2')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ExceptionNotSubmitted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('not_submiited', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ExceptionsNotApproved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exceptions_not_approved', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveSubmitted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_submitted', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OvertimeApproved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overtime_approved', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TotalExceptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
