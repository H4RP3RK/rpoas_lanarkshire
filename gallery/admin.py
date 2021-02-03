from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "location",
        "year",
        "caption",
        "image",
    )


admin.site.register(Image, ImageAdmin)
