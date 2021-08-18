from django import forms


class GetCallForm(forms.Form):
    select = forms.ChoiceField(label=None, choices=['Discussions with Financial Experts', 'Meet Finance Assistant - PR Agency',
                               'Discussions with Senior Finance Manager', 'Designer', 'Our CEO Finanace Theme Group'],
                               widget=forms.TextInput(attrs={
                                       'class': 'form-control custom-form custom-select'
                                   })
    )
    name = forms.CharField(max_length=150, label=None, widget= forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'name': 'name',
            'placeholder': 'Your Name: *',
        }),
    )
    phone = forms.IntegerField(label=None, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'phone',
            'name': 'phone',
            'placeholder': 'Phone Number: *',
        }),
    )

