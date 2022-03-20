from sre_parse import State
from django.db import models

from vendors.models import Vendor


# Create your models here.

class Resource(models.Model):
    # Resource fields here
    first_name = models.CharField(max_length=400)    
    last_name = models.CharField(max_length=400)
    title = models.CharField(max_length=400)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class Skill(models.Model):
    # Skill fields here
    skill_name = models.CharField(max_length=400)    
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class SkillLevel(models.Model):
    # Skill fields here
    skill_level = models.CharField(max_length=400)    
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class ResourceSkills(models.Model):
    # ResourceSkills fields here
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class ResourceSkillLevel(models.Model):
    # ResourceSkills fields here
    resource_skill_id = models.ForeignKey(ResourceSkills, on_delete=models.CASCADE)
    skill_level_id = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class ResourceAvailability(models.Model):
    # ResourceAvailability fields here
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    hours_per_day = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class ResourceCost(models.Model):
    # ResourceCost fields here
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    cost_per_hour = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

class ResourceTimeZone(models.Model):
    # ResourceTimeZone fields here
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    resource_time_zone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)