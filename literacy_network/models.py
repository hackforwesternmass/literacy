# Contains definitions of database entities
from django.db import models


class Volunteer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.

class CareerHistory(models.Model):
    pass 

class JobSector(models.Model):
    pass

class VolunteerSite(models.Model):
    pass

class Site(models.Model):
    pass

class HelpType(models.Model):
    pass

class HelpTypeResponse(models.Model):
    pass


