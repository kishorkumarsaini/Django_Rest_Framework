from django.contrib import admin
from song.models import Song,Singer
# Register your models here.

admin.site.register(Singer)
admin.site.register(Song)
