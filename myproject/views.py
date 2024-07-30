<<<<<<< HEAD
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#def login_view(request):
=======
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#def login_view(request):
>>>>>>> ea8a68fe7b0217bb4c2e78e8e5b70aeb0995d610
    return render(request, 'login_view.html')