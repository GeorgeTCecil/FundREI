from django import forms 
from .models import *

class ProjectForm(forms.ModelForm): 

    class Meta: 
        model = Project
        fields = ['title', 'location', 'units', 'price', 'roi', 'description', 'image'] 

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Location'}),
            'units': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Amount of Units in Project'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'roi': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the Project'}),
            
        }