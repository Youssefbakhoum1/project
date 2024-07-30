<<<<<<< HEAD
"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path




urlpatterns = [
        path('admin/', admin.site.urls),
   path('home/', views.homepage, name='homepage'),

    #path('login/', views.login_view, name='login_view'),
    path('about/', views.about, name='about'),
    path('posts/', include('posts.urls')),
   path('users/', include(('users.urls', 'users'), namespace='users')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
=======
"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path




urlpatterns = [
        path('admin/', admin.site.urls),
   path('home/', views.homepage, name='homepage'),

    #path('login/', views.login_view, name='login_view'),
    path('about/', views.about, name='about'),
    path('posts/', include('posts.urls')),
   path('users/', include(('users.urls', 'users'), namespace='users')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
>>>>>>> ea8a68fe7b0217bb4c2e78e8e5b70aeb0995d610
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)