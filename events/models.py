from django.db import models

# Create your models here.

class Event(models.Model):
    date = models.DateField()
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=150)
    content = models.TextField()
    place = models.CharField(max_length=30)
    headline = models.CharField(max_length=100)

    def __str__(self):
        return self.title