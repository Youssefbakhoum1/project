
# posts/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('posts_list/', views.posts_list, name='posts_list'),
        path('<slug:slug>', views.post_page, name='page'),
]