# pylint: disable=missing-module-docstring
from django.contrib import admin
from .models import Faqs

# Register your models here.
class FaqsAdmin(admin.ModelAdmin):
    """FAQ admin field list"""
    list_display = (
        "faq_title",
        "faq_content",
    )

    ordering = ('faq_title',)

admin.site.register(Faqs, FaqsAdmin)
