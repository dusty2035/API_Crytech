from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class New(models.Model):
    date = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/%Y/%m/%d/')
    excerpt = models.CharField(max_length=200)
    content = RichTextField()

    def __str__(self):
        return self.title