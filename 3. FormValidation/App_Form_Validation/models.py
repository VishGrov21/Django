from django.db import models

# Create your models here.


class Form_Model(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField()
    password = models.CharField(max_length=264)
