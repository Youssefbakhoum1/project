from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

#def login_view(request):
    return render(request, 'login_view.html')