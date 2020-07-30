'''
Created on 30 Jul 2020

@author: Gabriele Fantini
'''

from django import forms
from .models import Person 
import django_tables2 as tables

class InsertNewPersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = ["name", "date_of_birth", "email", "n_of_childs"]
        #temporary place holder to be replaced with datetime picker
        widgets = {
            'date_of_birth': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }

class PersonsTable(tables.Table):
    class Meta:
        model = Person