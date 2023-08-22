from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def default_time():
    return timezone.now().time()

from django.db import models

class Employee(models.Model):
    class Department(models.TextChoices):
        IT = 'IT', 'IT'
        SALES = 'S', 'Sales'
        MARKETING = 'MRKT', 'Marketing'
        HR = 'HR', 'Human Resources'

    class TimeCode(models.TextChoices):
        SHORT_TIME = 'ST', 'Short Time'
        NORMAL_TIME = 'NT', 'Normal Time'
        OVERTIME = 'OT', 'Overtime'

    class AttendanceCode(models.TextChoices):
        AT_WORK = 'AW', 'At Work'
        ON_LEAVE = 'OL', 'On Leave'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    department = models.CharField(
        max_length=4,
        choices=Department.choices,
        default=Department.SALES,
    )
    shift_date = models.DateField(default='2023-08-01')
    clocked_in = models.TimeField(null=True, default='08:00')
    clocked_out = models.TimeField(blank=True, null=True)
    time_authorized = models.TimeField(blank=True, null=True, default='09:00')

    time_code = models.CharField(
        max_length=3,
        choices=TimeCode.choices,
        default=TimeCode.NORMAL_TIME,
    )
    attendance_code = models.CharField(
        max_length=2,
        choices=AttendanceCode.choices,
        default=AttendanceCode.AT_WORK,
    )
    is_approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.clocked_out:
            self.clocked_out = datetime.now().time()  # Set the current time if not provided
        super().save(*args, **kwargs)
    
    def __str__(self):
        if self.name:
            return self.name
        else:
            return str(self.pk) 

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
    id
    shift_date
    clock_in
    clock_out

    class Meta:
        managed = False  # Set to False to prevent migrations for this model
        db_table = 'table_name_from_readonly_db'
        using = 'readonly_db'  # Use the database connection defined in settings

# Accessing Read-Only Data: You can now use the ReadOnlyModel to query and access the read-only data just like you would with any other Django model.

# Remember to set managed = False in the model's Meta class to prevent Django from creating migrations for this model since it's read-only.

# Keep in mind that while this approach allows you to integrate read-only data, you won't be able to use Django's built-in ORM to modify or save data to this model. It's meant specifically for querying and displaying data from a read-only source.

# Also, be cautious with your data source and connection settings, as read-only access should not unintentionally lead to any security issues or unintended modifications to the data.
"""
