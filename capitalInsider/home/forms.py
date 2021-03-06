from django import forms



class GetCallForm(forms.Form):
    OPTIONS = (
    ('Discussions with Financial Experts', 'Discussions with Financial Experts'),
    ('Meet Finance Assistant - PR Agency', 'Meet Finance Assistant - PR Agency'),
    ( 'Designer', 'Designer'),
    ('Discussions with Senior Finance Manager', 'Discussions with Senior Finance Manager'),
    ('Our CEO Finanace Theme Group', 'Our CEO Finanace Theme Group')
)

    select = forms.ChoiceField(label=None, choices=OPTIONS,
                               widget=forms.Select(attrs={
                                   'class': 'form-control custom-form custom-select'
                               }))
    name = forms.CharField(max_length=150, label=None, widget=forms.TextInput(attrs={
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
