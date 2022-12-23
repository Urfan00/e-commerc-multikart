from django import forms
from products.models import ProductReview


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['product_rate', 'name', 'email', 'review_title_1', 'review_title_2']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'review_title_1': "Review Title",
            'review_title_2': "Review Title"
        }
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"Enter your name",
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' :"E-mail"
                }
            ),
            'review_title_1' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : 1,
                    'placeholder' :"Enter your Review Subjects"
                }
            ),
            'review_title_2' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'rows' : 5,
                    'placeholder' :"Wrire Your Testimonial Here"
                }
            )
        }
