<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def logout_view(request):
    logout(request)
    return redirect('homepage')  # Adjust the redirect if needed

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('users:login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')  # Redirect to homepage or another page
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
=======
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def logout_view(request):
    logout(request)
    return redirect('homepage')  # Adjust the redirect if needed

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('users:login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')  # Redirect to homepage or another page
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
>>>>>>> ea8a68fe7b0217bb4c2e78e8e5b70aeb0995d610
