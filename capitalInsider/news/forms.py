from django import  forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["date"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'inputName',
                'type': "text",
                'placeholder': 'Your Name',
                'required': "required",
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'textarea',
                'required': "required",
                'rows': "5"
                }),
       }