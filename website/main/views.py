from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import SearchForm
from .models import Employee

# redirect to the following if not logged in
@login_required(login_url="/login")
def home(request):
    # Retrieve all employees from the database
    all_employees = Employee.objects.all()
    
    # Create a list of dictionaries, each representing an employee's data
    employees_as_dicts = []
    for employee in all_employees:
        employee_data = {
            'id': employee.id,
            'name': employee.name,
            'email': employee.email,
            'department': employee.department,
            'salary': employee.salary,
            'gender': employee.gender,
        }
        employees_as_dicts.append(employee_data)

     # Create a dictionary with the data to pass to the template
    context = {
        'employees': employees_as_dicts,
    }
    
    # Render the template with the context
    return render(request, 'main\home.html', context)

def sign_up(request):
    if request.method == 'POST':
        # take what is in the form and push it to the DB
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('/home')
    else:
        # give the user a blank form
        form = RegisterForm()
 
    return render(request, 'registration/sign_up.html', {"form": form})

# Search Popup
def searchView(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            employee_number = form.cleaned_data['employee_number']
            department = form.cleaned_data['department']
            
            # Query the database based on the form input
            results = Employee.objects.filter(
                start_date__gte=start_date,
                end_date__lte=end_date,
                employee_number__icontains=employee_number,
                department__icontains=department,
            )
            
            return render(request, 'main/search_results.html', {'results': results})
    else:  
        form = SearchForm()
    
    return render(request, 'main/search_form.html', {'form': form})