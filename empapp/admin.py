from django.contrib import admin
from empapp.models import employee

# Register your models here.

class employeeadmin(admin.ModelAdmin):
    emp_details=["empno","empname","empsalary","empaddress"]

admin.site.register(employee,employeeadmin)