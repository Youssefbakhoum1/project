from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateField()
    banner = models.ImageField(default='fallback.png', blank=True, )  # Provide a default value

    def __str__(self):
        return self.title
