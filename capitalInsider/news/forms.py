from django import  forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["date"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'yourName',
                'name': 'yourName',
                'placeholder': 'Your Name',
                }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'textarea',
                'name': 'comments',
                'rows': "6"
                }),
       }