from django.db import models

# Create your models here.
class Gallery(models.Model):
    """ registering images for the gallery """

    class Meta:
        verbose_name_plural = "Galleries"

    tag_line = models.CharField(max_length=254)
    alt = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.tag_line