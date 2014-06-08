# Contains definitions of database entities
from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField

class Industry(models.Model):
	"""Represents industries that volunteers may have experience in"""

	def __unicode__(self):
		return self.name

	name = models.CharField(max_length=100, verbose_name = 'industry name')
	code = models.CharField(max_length=10)

	class Meta:
		verbose_name_plural = "industries"

class Site(models.Model):
    """ Represents a location/office where a volunteer can participate """
    name = models.CharField(max_length=100, unique=True)
    

class Volunteer(models.Model):
    """ Represents a volunteer which has skills and time to donate """
    first_name = models.CharField(max_length=200, 
            verbose_name = 'volunteer\'s first name')
    last_name = models.CharField(max_length=200, 
            verbose_name = 'volunteer\'s last name')
    phone = models.CharField(max_length=12, verbose_name = 'volunteer\'s phone number')

    address_line1 = models.CharField(max_length=100, null=True, blank=True)
    address_line2 = models.CharField(max_length=100, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)

    occupation_notes = models.TextField(null=True, blank=True)
    volunteer_notes = models.TextField(null=True, blank=True)

    is_public = models.BooleanField(default=False)
    linkedin_link = models.CharField(max_length=100, null=True, blank=True)

    user = models.ForeignKey(User, null=True, blank=True)

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

    # indicates if the volunteer is willing to go to the site
    affirmative = models.BooleanField()

    def __unicode__(self):
        return unicode(self.site.name)

class HelpType(models.Model):
    """ A type of participation that a volunteer is willing to """
    short_name = models.CharField(max_length=10)
    description = models.CharField(max_length=150)
    has_details = models.BooleanField()
    help_text = models.CharField(max_length=500)

class HelpTypeResponse(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    affirmative = models.BooleanField(default=False)
    help_type = models.ForeignKey(HelpType)
    details = models.TextField(null=True, blank=True)


