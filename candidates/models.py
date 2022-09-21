from distutils.command.upload import upload
from django.db import models

# Create your models here.




class Candidates(models.Model):
    name = models.CharField(max_length=200)
    political_party = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='uploads/')




    def __str__(self):
        return self.name

