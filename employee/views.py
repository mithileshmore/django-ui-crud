from django.shortcuts import render, redirect
from django.http import HttpResponse
from employee.models import Employee
from employee.forms import EmployeeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return HttpResponse('Hello')


def show(request):
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  


def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:  
                form.save()  
                return redirect('/')  
            except:  
                print('Something went wrong')
    else:
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form}) 


def edit(request, id):
    if request.method == 'POST':
        employee = Employee.objects.get(id=id)  
        form = EmployeeForm(request.POST, instance = employee)  
        if form.is_valid():  
            form.save()  
            return redirect('/')  
        return render(request, 'edit.html', {'employee': employee})
    else:
        employee = Employee.objects.get(id=id)
        return render(request,'edit.html', {'employee':employee})


def delete(request, id):
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})