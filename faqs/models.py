from django.db import models

# Create your models here.
class Faqs(models.Model):
    """ registering images for the gallery """

    class Meta:
        verbose_name_plural = "faqs"

    faq_title = models.CharField(max_length=254)
    faq_content = models.CharField(max_length=254)

    def __str__(self):
        return self.faq_title