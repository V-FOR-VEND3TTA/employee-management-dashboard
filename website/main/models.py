from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    employee_number = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    shift_date = models.DateField()
    clocked_in = models.DateTimeField()
    clocked_out = models.DateTimeField()
    time_code = models.CharField(max_length=20, choices=[('TC1', 'Time Code 1'), ('TC2', 'Time Code 2')])
    attendance_code = models.CharField(max_length=20, choices=[('AC1', 'Attendance Code 1'), ('AC2', 'Attendance Code 2')])
    
    def __str__(self):
        return self.employee_number
