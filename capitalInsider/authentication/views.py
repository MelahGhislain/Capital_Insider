from django.shortcuts import render,  redirect
from .forms import CreateUserForm
from  django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        else:
            messages.info(request, "username or password incorrect")

    return render(request, 'authenticate/login.html')


def signUpPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f"Account created successfully for {username}")
            return redirect('login')
    context = {"form": form}
    return render(request, 'authenticate/signup.html', context)


def forgotPassword(request):
    return render(request, 'authenticate/forgot-password.html')

def logoutUser(request):
    logout(request)
    return redirect('login')