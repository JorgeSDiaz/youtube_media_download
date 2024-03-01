from django.db import models


# Create your models here.
class VideoRequest(models.Model):
    url = models.TextField(max_length=1000, blank=False, null=False)
