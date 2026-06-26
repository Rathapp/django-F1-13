from django import forms
from .models import Patient

class patientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields='__all__'

        widgets = {
        'firstName' : forms.TextInput( attrs={ 'class': 'form-control','placeholder':'First name' }),
        'lastName' : forms.TextInput( attrs={ 'class': 'form-control','placeholder':'Last name' }),
        'sex' : forms.Select( attrs={ 'class': 'form-control' }),
        'dob' : forms.DateInput( attrs={ 'class': 'form-control','type':'date' }),
        'pob' : forms.TextInput(attrs={'class':'form-control'}),
        'address' : forms.TextInput(attrs={'class':'form-control'}),
        'profileImage': forms.FileInput(attrs={ 'class': 'form-control','type':'file' }),
        'is_active': forms.CheckboxInput(attrs={ 'class':'form-check-input'})

         }   