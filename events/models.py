from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=500)
    location = models.CharField(max_length=500, null=True, blank=True)
    lat = models.DecimalField(max_digits=15, decimal_places=7, null=True, blank=True)
    lng = models.DecimalField(max_digits=15, decimal_places=7, null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title