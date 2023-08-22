from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display= ["id", "name", "time_authorized", "is_approved"]
    search_fields = ['id', 'name']
    list_per_page = 8


admin.site.register(Employee, EmployeeAdmin)
