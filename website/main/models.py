from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    DEPARTMENT = (
        ('IT', 'IT'),
        ('Sales', 'Sales'),
        ('Marketing', 'Marketing'),
        ('HR', 'Human Resources'),
    )
    department = models.CharField(max_length=100, null=True, choices=DEPARTMENT)
    salary = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, null=True, choices=GENDER)

    def __str__(self):
        return self.name

"""
# muted version of employee class
class Employee(models.Model):
    name = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    DEPARTMENT = (
        ('IT', 'IT'),
        ('Sales', 'Sales'),
        ('Marketing', 'Marketing'),
        ('HR', 'Human Resources'),
    )
    department = models.CharField(max_length=100, null=True, choices=DEPARTMENT)
    shift_date = models.DateField()
    clocked_in = models.DateTimeField()
    clocked_out = models.DateTimeField()
    time_approved = models.TimeField(blank=True, null=True)
    TIMECODE = (
        ('ST', 'Short Time'),
        ('NT', 'Normal Time'),
        ('OT', 'Overtime'),
    )
    time_code = models.CharField(max_length=20, choices=TIMECODE)
    attendance_code = models.CharField(max_length=20, choices=[('AW', 'At Work'), ('OL', 'On Leave')])
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.employee_name # What we'll be using as part of a search field
"""

# All the exceptions that will appear on the dashboard
class TotalExceptions(models.Model):
    total_no = models.CharField(max_length=10)

    def __str__(self):
        return self.total_no

class ExceptionNotSubmitted(models.Model):
    not_submiited = models.CharField(max_length=10)

    def __str__(self):
        return self.not_submiited

# Exceptions submitted but not approved
class ExceptionsNotApproved(models.Model):
    exceptions_not_approved = models.CharField(max_length=10)

    def __str__(self):
        return self.exceptions_not_approved

class OvertimeApproved(models.Model):
    overtime_approved = models.CharField(max_length=10)

    def __str__(self):
        return self.overtime_approved

class LeaveSubmitted(models.Model):
    leave_submitted = models.CharField(max_length=10)

    def __str__(self):
        return self.leave_submitted


# FOR READ ONLY 
# e.g. Emp No, Shift Date, Clock In, Clock Out
"""
class ReadOnlyModel(models.Model):
    # Fields here

    class Meta:
        managed = False  # Set to False to prevent migrations for this model
        db_table = 'table_name_from_readonly_db'
        using = 'readonly_db'  # Use the database connection defined in settings

# Accessing Read-Only Data: You can now use the ReadOnlyModel to query and access the read-only data just like you would with any other Django model.

# Remember to set managed = False in the model's Meta class to prevent Django from creating migrations for this model since it's read-only.

# Keep in mind that while this approach allows you to integrate read-only data, you won't be able to use Django's built-in ORM to modify or save data to this model. It's meant specifically for querying and displaying data from a read-only source.

# Also, be cautious with your data source and connection settings, as read-only access should not unintentionally lead to any security issues or unintended modifications to the data.
"""

# the workspace that will display all the info we're looking for 
"""class Workspace(models.Model):
    employee_number = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=100) # must inherit 
    email = models.EmailField(max_length=30)
    DEPARTMENT = (
        ('IT', 'IT'),
        ('Sales', 'Sales'),
        ('Marketing', 'Marketing'),
        ('HR', 'Human Resources'),
    )
    department = models.CharField(max_length=100, null=True, choices=DEPARTMENT)
    start_date = models.DateField()
    end_date = models.DateField()
    shift_date = models.DateField()
    clocked_in = models.DateTimeField()
    clocked_out = models.DateTimeField()
    time_approved = models.TimeField(blank=True, null=True)
    TIMECODE = (
        ('ST', 'Short Time'),
        ('NT', 'Normal Time'),
        ('OT', 'Overtime'),
    )
    time_code = models.CharField(max_length=20, choices=TIMECODE)
    attendance_code = models.CharField(max_length=20, choices=[('AW', 'At Work'), ('OL', 'On Leave')])
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.employee_name # What we'll be using as part of a search field
"""