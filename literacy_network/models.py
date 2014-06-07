# Contains definitions of database entities
from django.db import models

class Industry(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

class Site(models.Model):
    """ Represents a location/office where a volunteer can participate """
    name = models.CharField(max_length=100)

class Volunteer(models.Model):
    """ Represents a volunteer which has skills and time to donate """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30, null=True, blank=True)

    address_line1 = models.CharField(max_length=100, null=True, blank=True)
    address_line2 = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)

    notes = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=False)
    linkedin_link = models.CharField(max_length=100, null=True, blank=True)

class Occupation(models.Model):
    """ An occupation held by a volunteer for some time period """
    volunteer = models.ForeignKey(Volunteer)
    job_title = models.CharField(max_length=50)
    industry = models.ForeignKey(Industry, verbose_name="Industry")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class VolunteerSite(models.Model):
    """ Mapping between volunteers and the sites they work at """
    volunteer = models.ForeignKey(Volunteer)
    site = models.ForeignKey(Site)

class HelpType(models.Model):
    """ A type of participation that a volunteer is willing to """
    description = models.CharField(max_length=150)

class HelpTypeResponse(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    affirmative = models.BooleanField()
    help_type = models.ForeignKey(HelpType)


