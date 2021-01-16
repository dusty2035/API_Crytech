from django.db import models

# Create your models here.

class Game(models.Model):
    background_img = models.ImageField(upload_to='images/')
    main_img = models.ImageField(upload_to='images/')
    name_img = models.ImageField(upload_to='images/')
    alt_text = models.CharField(max_length=50)
    game_title = models.CharField(max_length=50)
    game_description = models.TextField()
    release_date = models.DateField('')
    publisher_1 = models.CharField(max_length=50)
    publisher_1_anchor = models.URLField()
    publisher_2 = models.CharField(max_length=50 , blank=True)
    publisher_2_anchor = models.URLField( blank=True)
    publisher_3 = models.CharField(max_length=50, blank=True)
    publisher_3_anchor = models.URLField( blank=True)
    trailer_url = models.URLField()
    platform_1 = models.CharField(max_length=20)
    platform_1_anchor = models.URLField()
    platform_2 = models.CharField(max_length=20, blank=True)
    platform_2_anchor = models.URLField(blank=True)
    platform_3 = models.CharField(max_length=20, blank=True)
    platform_3_anchor = models.URLField(blank=True)


    def __str__(self):
        return self.game_title