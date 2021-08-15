from django.db import models
from django.urls import reverse



# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse('detail', args=(str(self.id)) )
        return reverse('home')
