from django.contrib import admin
from .models import Resource, Skill, Availability, Booking

# Register your models here.
admin.site.register(Resource)
admin.site.register(Skill)
admin.site.register(Availability)
# admin.site.register(Booking)