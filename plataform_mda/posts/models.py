#Posts Models

# Django
from django.db import models


class Posts(models.Model):
    
    
    title = models.CharField(max_length=255)
    website = models.URLField(max_length=200, blank=True)
    details = models.TextField(blank=True)
    
    photo = models.ImageField(
        upload_to='static/img/',
        blank=True,
        null=True,
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return Title """
        return self.title