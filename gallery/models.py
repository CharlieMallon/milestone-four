from django.db import models

# Create your models here.
class Gallery(models.Model):
    """ registering images for the gallery """

    class Meta:
        verbose_name_plural = "Galleries"

    tag_line = models.CharField(max_length=254, null=False, blank=False)
    alt = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.tag_line