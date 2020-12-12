from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField()
    location = models.CharField(max_length=500, null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title