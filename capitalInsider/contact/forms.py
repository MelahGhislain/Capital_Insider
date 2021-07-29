from django import forms
from .models import MailUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = MailUs
        fields = "__all__"
        error_messages = {
            'user_name': {
                'required': 'Please enter your name'
            }
        }
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'yourName',
                'name': 'yourName',
                'placeholder': 'Your Name',
                }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'yourEmail',
                'name': 'yourEmail',
                'placeholder': 'Your Email',
                }),
            'phone_num': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phoneNumber',
                'name': 'phoneNumber',
                'placeholder': 'Phone Number',
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'textarea',
                'name': 'comments',
                'placeholder': 'Your Messages',
                'rows': "6"
                }),
       }


class ContactForm(forms.ModelForm):
    pass