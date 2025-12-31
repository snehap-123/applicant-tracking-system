# Create your models here.
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
