from sre_parse import State
from django.db import models


# Create your models here.

class Vendor(models.Model):
    # vendor fields here
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)