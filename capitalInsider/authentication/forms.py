from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class  Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']