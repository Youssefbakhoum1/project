<<<<<<< HEAD
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateField()
    banner = models.ImageField(default='fallback.png', blank=True, )  # Provide a default value

    def __str__(self):
        return self.title
=======
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateField()
    banner = models.ImageField(default='fallback.png', blank=True, )  # Provide a default value

    def __str__(self):
        return self.title
>>>>>>> ea8a68fe7b0217bb4c2e78e8e5b70aeb0995d610
