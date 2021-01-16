from django.contrib import admin
from django.utils.html import format_html
from .models import Game
# Register your models here.

class GameAdmin(admin.ModelAdmin):

    def thumbnail(self , object):
        return format_html(f'<img src="{object.main_img.url}" width="100" style="border-radius: 10px" />')


    thumbnail.short_description = 'Game Picture'

    list_display = ('thumbnail' , 'game_title', 'publisher_1')
    list_display_links = ( 'thumbnail', 'game_title', )
    search_fields = ('game_title',)
    list_filter = ('game_title',)
    

admin.site.register(Game , GameAdmin)