from django import forms
from .models import MailUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = MailUs
        fields = "__all__"