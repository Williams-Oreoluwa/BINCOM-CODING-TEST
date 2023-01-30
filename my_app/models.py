from django.db import models

# Create your models here.

class Parties_result(models.Model):
    Party = models.TextField()
    Result = models.IntegerField()
    