from django.contrib import admin
from .models import Gallery

# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        "tag_line",
		"alt",
		"image",
    )

    ordering = ('tag_line',)

admin.site.register(Gallery, GalleryAdmin)