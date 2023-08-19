from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput     
from .models import Employee 

# Search popup 
class SearchForm(forms.Form):
    start_date = forms.DateField(label='Start Date', required=True, widget= DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', required=True, widget=DateInput(attrs={'type': 'date'}))
    employee_number = forms.CharField(label='Employee Number', required=False, widget = forms.TextInput(attrs={'placeholder':'Enter employee number'}))
    department = forms.CharField(label='Department', max_length=50, required=False) 


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget = forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    last_name = forms.CharField(required=True, widget = forms.TextInput(attrs={'placeholder':'Enter your last name'}))
    username = forms.CharField(max_length = 100, required=True, widget = forms.TextInput(attrs={'placeholder':'Enter the name you want to use when you log on'}))                           
    email = forms.EmailField(required=True, widget = forms.TextInput(attrs={'placeholder':'Enter your email address'}))
    password1 = forms.CharField(max_length=13, required=True, widget = forms.TextInput(attrs={'placeholder':'Enter your password'}))
    password2 = forms.CharField(max_length=13, required=True, widget = forms.TextInput(attrs={'placeholder':'Confirm your password'}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
