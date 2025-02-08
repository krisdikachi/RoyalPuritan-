from django.db import models
from django.contrib.auth.models import User


class SlideshowImage2(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slideshow_images/')
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class SlideshowImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slideshow_images/')
    caption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# Compare this snippet from RoyalPuritan/RoyalWebpage/admin.py: