from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    title = models.CharField(max_length=100)
    studentNumber= models.IntegerField(null=True)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='HomeWorks/pdfs/')


    def __str__(self):
        return self.title



class HomeWork(models.Model):
    title = models.CharField(max_length=100)
    deadline= models.DateField(null=True)
    tozihat = models.CharField(max_length=512,null=True)
    pdf = models.FileField(upload_to='my_home_works/pdfs/')

    def __str__(self):
        return self.title



#class Video(models.Model):
#   title = models.CharField(max_length=100)
#    video= models.FileField(upload_to='watchVideo/videos/')

#   def __str__(self):
#       return self.title