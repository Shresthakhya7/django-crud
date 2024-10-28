from django.db import models

# Create your models here.
class Destinations(models.Model):
    destination_name=models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.destination_name
    
class Guide(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    