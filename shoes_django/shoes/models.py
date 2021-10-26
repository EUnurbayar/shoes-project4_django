from django.db import models

# Create your models here.

class Shoes(models.Model):
    type = models.CharField(max_length=100)
    styling = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    brand_url = models.TextField()

    def __str__(self):
        return self.type