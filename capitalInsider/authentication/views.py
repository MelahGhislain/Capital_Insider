from django.shortcuts import render
from .forms import CreateUserForm

# Create your views here.
def loginPage(request):
    return render(request, 'authenticate/login.html')


def signUpPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, 'authenticate/signup.html', context)


def forgotPassword(request):
    return render(request, 'authenticate/forgot-password.html')