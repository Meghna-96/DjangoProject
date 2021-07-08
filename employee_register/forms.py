from django import forms
from django.db.models import fields
from .models import Employee

class EmployeeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['Position'].empty_label = "Select"
        self.fields['PhoneNo'].required = False


    class Meta:
        model = Employee
        fields= '__all__'
        labels = {
            'PhoneNo': 'Phone Number'
        }