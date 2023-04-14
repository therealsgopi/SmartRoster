from django.db import models

# Create your models here.

class class_image(models.Model):
    # title = models.CharField(max_length=100)
    # content = models.TextField()
    image = models.ImageField(upload_to='class_images')
    
    def __str__(self):
        return self.title