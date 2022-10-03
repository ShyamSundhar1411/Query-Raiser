from . models import *
from django import forms

class QueryCreateForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['title','type','description','department']
