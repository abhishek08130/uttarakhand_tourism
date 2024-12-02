from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    image = models.URLField()
    image2 = models.URLField(null=True, blank=True)
    tourplan = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class sub(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email