from __future__ import unicode_literals

from django.db import models

class SavedUser(models.Model):
    source = models.CharField(max_length=16)
    handle = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    influencer = models.CharField(max_length=16)
    followers = models.IntegerField()
    following = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.handle

# Create your models here.
