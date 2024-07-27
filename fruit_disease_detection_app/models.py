from django.db import models

# Create your models here.
class Image(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'uploads/', default = '')
    def __str__(self):
        return self.description
    
