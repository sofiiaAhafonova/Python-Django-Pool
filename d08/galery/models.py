from django.db import models

# Create your models here.
class  GaleryModel(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
