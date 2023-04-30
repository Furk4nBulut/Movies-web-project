from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100,verbose_name='Movie Name')
    description = models.TextField(verbose_name='Film description')
    image = models.CharField(max_length=50,verbose_name='Film image')
    created_date= models.DateTimeField(auto_now_add=True,verbose_name='Film create date')
    isPublished = models.BooleanField(default=True)

    def __str__(self):
        return  self.name
    def get_image_path(self):
        return '/img/'+self.image
