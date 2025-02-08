from django.contrib import admin

# filepath: /c:/Users/HP/OneDrive/Desktop/AndroTechlist/RoyalPuritan/imageapp/admin.py
from django.contrib import admin
from .models import SlideshowImage

@admin.register(SlideshowImage)
class SlideshowImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption')
# Register your models here.
