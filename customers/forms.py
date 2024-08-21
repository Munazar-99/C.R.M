from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["customer_id", "first_name", "last_name", "email", "phone_number"]
        labels = {
            "customer_id": "Customer Number",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
        }
        widgets = {
            "customer_id": forms.NumberInput(attrs={'class': 'form-control'}),
            "first_name":  forms.TextInput(attrs={'class': 'form-control'}),
            "last_name":  forms.TextInput(attrs={'class': 'form-control'}),
            "email":  forms.EmailInput(attrs={'class': 'form-control'}),
            "phone_number":  forms.NumberInput(attrs={'class': 'form-control'}),
        }
