from django import forms
from django.forms import ModelForm
from .models import postgmodels
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


 #this is for the date field in models
class dateinput(forms.DateInput):
    input_type = 'date'


class postgform(forms.ModelForm):
    
    class Meta:
        model= postgmodels
        fields= ['title', 'comment', 'created', 'date_of_birth']
        widgets = {'date_of_birth': dateinput}

        



class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']