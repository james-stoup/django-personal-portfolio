from django.db import models

# Create your models here.
from django.db import models

from datetime import datetime

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')
    url = models.URLField(blank=True)
    date = models.DateField()
    
    def __str__(self):
        return self.title
