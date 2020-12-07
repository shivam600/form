from django.shortcuts import render,redirect
from .forms import DestinationForm
from .models import Destination

# Create your views here.
def employee_list(request):
    context={"employee_list":Destination.objects.all()}
    return render(request,"employee_register/employee_list.html",context)
def employee_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form=DestinationForm()
        else:
            employee=Destination.objects.get(pk=id)  
            form=DestinationForm(instance=employee)  
        return render(request,"employee_register/employee_form.html",{"form":form})
    else:
        if id==0:
            form=DestinationForm(request.POST)
        else:
            employee=Destination.objects.get(pk=id)  
            form=DestinationForm(request.POST,instance=employee)  
        if form.is_valid():
            form.save()
        return redirect("/employee/list")    

def employee_delete(request,id):
    employee=Destination.objects.get(pk=id)  
    employee.delete()
    return redirect("/employee/list") 

  
