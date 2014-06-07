from django import forms
from literacy_network.models import *
from django.forms.models import modelformset_factory, inlineformset_factory

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer

class UserForm(forms.ModelForm):
    class Meta:
        model = User

class OccupationForm(forms.ModelForm):
    class Meta:
        model = Occupation
        exclude = ['start_date', 'end_date']

HelpResponseFormset = inlineformset_factory(
    Volunteer, HelpTypeResponse, extra=3, can_delete=False)
OccupationFormset = inlineformset_factory(
    Volunteer, Occupation, form=OccupationForm, extra=3, can_delete=False)
SiteForm = inlineformset_factory(
    Volunteer, VolunteerSite, extra=0, can_delete=False)



