from sre_parse import State
from django.db import models


# Create your models here.

class Vendor(models.Model):
    # vendor fields here
    first_name = models.CharField(max_length=400)    
    last_name = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    business_name = models.CharField(max_length=400)
    business_website = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

def __str__(self):
        return self.business_name