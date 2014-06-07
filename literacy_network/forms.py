from django import forms
from literacy_network.models import *
from django.forms.models import modelformset_factory, inlineformset_factory

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
