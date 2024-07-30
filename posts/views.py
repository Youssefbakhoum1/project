<<<<<<< HEAD
# posts/views.py
from django.shortcuts import render
from .models import Post

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html',{ 'posts':posts})
def post_page(request,slug):
    posts = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html',{ 'post':posts})


# posts/views.py

=======
# posts/views.py
from django.shortcuts import render
from .models import Post

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html',{ 'posts':posts})
def post_page(request,slug):
    posts = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html',{ 'post':posts})


# posts/views.py

>>>>>>> ea8a68fe7b0217bb4c2e78e8e5b70aeb0995d610
