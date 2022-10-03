from . models import *
from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class QueryCreateForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['title','type','description']
class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    email = forms.CharField(disabled=True)
    first_name = forms.CharField(disabled=True)
    last_name = forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
class ProfileForm(forms.ModelForm):
    contact = PhoneNumberField(required = True)
    role = forms.CharField(disabled=True)
    department = forms.CharField(disabled=True,required=False)    
    admitted_year = forms.CharField(disabled=True,required=False) 
    class Meta:
        model = Profile
        fields = ['role','contact','department','admitted_year']