from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from datetime import datetime, timedelta
from django.db import DatabaseError
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from literacy_network.models import *
from literacy_network.forms import *
import csv, sys, os

def edit_volunteer(request, volunteer_id=None):
    """ Presents a view used to edit a volunteer

        Keyword arguments:
            volunteer_id -- The primary key of the volunteer
                        to edit, or None to perform an add
        Returns a view used to edit the volunteer on GET,
            or a redirection to the volunteer list on POST
    """
    print("Volunteer with id {0} requested".format(volunteer_id))
    volunteer = None
    try:
        volunteer = Volunteer.objects.get(id=volunteer_id)
    except Volunteer.DoesNotExist:
        print("Volunteer with id {0} does not exist".format(volunteer_id))
        vol_form = VolunteerForm()
        resp_form = HelpResponseForm()
        occ_form = OccupationForm()

    if request.method == "POST":
        vol_form = VolunteerForm(request.POST, request.FILES, instance=volunteer)
        resp_form = HelpResponseForm(request.POST, request.FILES, instance=volunteer)
        occ_form = OccupationForm(request.POST, request.FILES, instance=volunteer)
        if vol_form.is_valid() and resp_form.is_valid() and occ_form.is_valid():
            svol = vol_form.save()
            sresp = resp_form.save()
            socc = occ_form.save() 
    elif volunteer_id:
        vol_form = VolunteerForm(instance=volunteer)
        resp_form = HelpResponseForm(instance=volunteer)
        occ_form = OccupationForm(instance=volunteer)

    return render(request, 'edit-volunteer.html', 
        {"vol_form" : vol_form, "resp_form" : resp_form, "occ_form" : occ_form})

def volunteers(request):
    """ Presents a list of volunteers """
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers.html',
            {"volunteers" : volunteers})

