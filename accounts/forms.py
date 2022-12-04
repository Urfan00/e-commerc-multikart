from django import forms
from .models import Personal_detail, Shipping_address
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordResetForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : _('Enter your username')
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder' : _('Password')
            }
        )
    )


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : _("Your password")
            }
        ),
        label=_('Password')
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : _("Confirm password")
            }
        ),
        label=_('Confirm Password')
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : _("Enter your first name"),
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : _("Enter your last name")
                }
            ),
            'username' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : _("Username")
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"E-mail"
                }
            ),
        }


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder' : 'Enter Your E-mail'
            }
        )
    )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(required=True, label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your New Password'
            }))
    new_password2 = forms.CharField(required=True, label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Your New Password'
            }))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, label='Old Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Old Password'
            }))
    new_password1 = forms.CharField(required=True, label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your New Password'
            }))
    new_password2 = forms.CharField(required=True, label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Your New Password'
            }))


# ************************************************************************************


class PersonalDetailFormModel(forms.ModelForm):
    class Meta:
        model = Personal_detail
        exclude = ['user_id']
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


class ShippingAddressFormModel(forms.ModelForm):
    class Meta:
        model = Shipping_address
        exclude = ['user_id']
        labels = {
            'company_name' : 'Flat / Plot',
            'address' : 'Address',
            'postal_code' : 'Zip Code',
            'city' : 'City',
            'region_state' : 'Region/State '
        }
        widgets = {
            'company_name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your company name",
                }
            ),
            'address' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your address",
                }
            ),
            'postal_code' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"zip-code",
                }
            ),
            'Country' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your country",
                }
            ),
            'city' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your city",
                }
            ),
            'region_state' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Region/State",
                }
            )
        }

