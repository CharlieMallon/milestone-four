from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=254, null=True, blank=True, editable=True)
    message_text = models.TextField(null=True, blank=True, editable=True)
    date = models.DateTimeField(auto_now_add=True)
    message_status = models.CharField(max_length=10, null=True, blank=True, default="Not Sent")

    def __str__(self):
        return self.subject