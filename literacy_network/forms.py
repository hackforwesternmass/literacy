from django import forms
from literacy_network.models import *
from django.forms.models import modelformset_factory, inlineformset_factory

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer

class UserForm(forms.ModelForm):
    class Meta:
        model = User

HelpResponseFormset = inlineformset_factory(
    Volunteer, HelpTypeResponse, extra=3, can_delete=False)
OccupationFormset = inlineformset_factory(
    Volunteer, Occupation, extra=3, can_delete=False)
SiteForm = inlineformset_factory(
    Volunteer, VolunteerSite, extra=0, can_delete=False)



