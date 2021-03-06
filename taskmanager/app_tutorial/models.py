from django.contrib.auth.models import User
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_stars = models.IntegerField(default=5)
    number_rooms = models.IntegerField(default=3)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.hotel}, {self.user}'

