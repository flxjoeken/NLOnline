from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, UsernameField
from django.contrib.auth.models import User

from nlonline_antrag.fields import StudEmailField
from nlonline_antrag.models import NLOnlineAntrag


class NLForm(forms.ModelForm):
    class Meta:
        model = NLOnlineAntrag
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{5}'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'application_date_bafoeg': forms.DateInput(attrs={'class': 'form-control'}),
            'account_holder': forms.TextInput(attrs={'class': 'form-control'}),
            'iban': forms.TextInput(attrs={'class': 'form-control'}),
            'bic': forms.TextInput(attrs={'class': 'form-control'}),

            'signed_form': forms.FileInput(attrs={'class': 'form-control'}),
            'health_insurance_certificate': forms.FileInput(attrs={'class': 'form-control'}),
            'enrollment_certificate': forms.FileInput(attrs={'class': 'form-control'}),
            'identity_document': forms.FileInput(attrs={'class': 'form-control'}),
            'bank_statements': forms.FileInput(attrs={'class': 'form-control'}),
        }


class RegisterForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {"username": UsernameField,
                         "email": StudEmailField}
