from django import forms
from .models import Contact
from django.utils.translation import gettext as _



class ContactFormModel(forms.ModelForm):
    class Meta:
        model = Contact
        fields ='__all__'
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email' : 'Email',
            'phone_number' : 'Phone number',
            'message' : 'Message'
        }
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your first name",
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your last name"
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"E-mail"
                }
            ),
            'phone_number' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your number"
                }
            ),
            'message' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : 7,
                    'placeholder' :"Write your message"
                }
            ),
        }
