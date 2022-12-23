from django import forms

from .models import BillingAddress


class BillingAddressFromModel(forms.ModelForm):
    class Meta:
        model = BillingAddress
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'phone' : 'Phone',
            'email_address' : 'Email Address',
            'address' : 'Address',
            'town_city' : 'Town/City',
            'state_county' : 'State / County',
            'postal_code' : 'Postal Code'
        }
        exclude = ['user_id']
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'class' : 'form-label',
                    'placeholder' :"Enter your first name",
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'class' : 'form-label',
                    'placeholder' :"Enter your last name"
                }
            ),
            'phone' : forms.TextInput(
                attrs={
                    'class' : 'form-label',
                    'placeholder' :"Enter your number"
                }
            ),
            'email_address' : forms.EmailInput(
                attrs={
                    'class' : 'form-label',
                    'placeholder' :"E-mail"
                }
            ),
            'country' : forms.TextInput(
                attrs={
                    'class' : 'form-label',
                    'placeholder' :"Enter your country",
                }
            ),
            'address' : forms.TextInput(
                attrs={
                    'class' : 'form-label',
                    'placeholder' :"Street address",
                }
            ),
            'town_city' : forms.TextInput(
                attrs={
                    'class' : 'form-label',
                    'placeholder' :"Enter your city",
                }
            ),
            'state_county' : forms.TextInput(
                attrs={
                    'class' : 'form-label',
                    'placeholder' :"Enter your state",
                }
            ),
            'postal_code' : forms.TextInput(
                attrs={
                    'class' : 'form-label',
                    'placeholder' :"Enter your zip code",
                }
            ),
        }
