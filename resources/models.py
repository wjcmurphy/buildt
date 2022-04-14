from datetime import timezone
from operator import mod
from pyexpat import model
from sre_parse import State
from django.db import models

from vendors.models import Vendor

# Create your models here.
class Skill(models.Model):
    # Skill fields here
    skill_name = models.CharField(max_length=400)  
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self):
        return self.skill_name

class Availability(models.Model):
    # ResourceAvailability fields here
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hours_per_day = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Resource(models.Model):
    # Resource fields here
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    title = models.CharField(max_length=400)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    availability = models.ManyToManyField(Availability)
    time_zone = models.CharField(max_length=25, default='cst')
    cost_per_hour = models.FloatField(default=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

# class SkillLevel(models.Model):
#     # Skill fields here
#     skill_level = models.CharField(max_length=400)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True)

# class ResourceSkills(models.Model):
#     # ResourceSkills fields here
#     resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
#     skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True)

# class ResourceSkillLevel(models.Model):
#     # ResourceSkills fields here
#     resource_skill = models.ForeignKey(ResourceSkills, on_delete=models.CASCADE)
#     skill_level = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True, blank=True)