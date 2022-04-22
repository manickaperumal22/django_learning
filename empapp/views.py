from django.shortcuts import render
from empapp.models import employee

# Create your views here.
def empdetails(request):
    emp_data=employee.objects.all()
    emp_dict={"emp_list":emp_data,"name":"manic"}
    return render(request,"empapp/abc.html",context=emp_dict)