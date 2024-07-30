<<<<<<< HEAD
# posts/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('posts_list/', views.posts_list, name='posts_list'),
        path('<slug:slug>', views.post_page, name='page'),
]
=======
# posts/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('posts_list/', views.posts_list, name='posts_list'),
        path('<slug:slug>', views.post_page, name='page'),
]
>>>>>>> ea8a68fe7b0217bb4c2e78e8e5b70aeb0995d610
