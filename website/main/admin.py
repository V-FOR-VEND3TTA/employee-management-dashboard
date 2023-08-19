from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display= ["name", "email", "department", "gender"]
    search_fields = ['name']
    list_per_page = 8


admin.site.register(Employee, EmployeeAdmin)
