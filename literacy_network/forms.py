from django import forms
from literacy_network.models import *
from django.forms.models import modelformset_factory, inlineformset_factory

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer

HelpResponseForm = inlineformset_factory(
    Volunteer, HelpTypeResponse, extra=0, can_delete=False)
OccupationForm = inlineformset_factory(
    Volunteer, Occupation, extra=0, can_delete=False)
SiteForm = inlineformset_factory(
    Volunteer, VolunteerSite, extra=0, can_delete=False)
    



