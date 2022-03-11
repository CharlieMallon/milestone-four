# pylint: disable=missing-module-docstring
from django.contrib import admin
from .models import Gallery

# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    """
    List out the items in gallery Admin
    """
    list_display = (
        "tag_line",
		"alt",
		"image",
    )

    ordering = ('tag_line',)

admin.site.register(Gallery, GalleryAdmin)
