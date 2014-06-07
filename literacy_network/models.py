# Contains definitions of database entities
from django.db import models


class Volunteer(models.Model):
    """ Represents a volunteer which has skills and time to donate """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=False)
    linkedin_link = models.CharField(max_length=100)

class Occupation(models.Model):
    """ An occupation held by a volunteer for some time period """
    volunteer = models.ForeignKey(Volunteer)
    job_title = models.CharField(max_length=50)
    job_sector = models.ForeignKey(JobSector, verbose_name="Job Sector")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

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


