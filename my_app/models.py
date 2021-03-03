from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='HomeWorks/pdfs/')

    def __str__(self):
        return self.title

