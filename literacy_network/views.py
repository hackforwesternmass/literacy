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
        form = VolunteerForm()

    if request.method == "POST":
        form = VolunteerForm(request.POST, request.FILES, instance=volunteer)
        if form.is_valid():
            svol = form.save()
    elif volunteer_id:
        form = VolunteerForm(instance=volunteer)

    return render(request, 'edit-volunteer.html',

        {"form" : form})
def upload_industries(request):
	'''Handles upload of industry data in CSV format'''
	for row in csv.DictReader(request.FILES["industries-csv"]):
		industry = Industry()
		industry.code=row["Industry_Code"]
		industry.name=row["Industry_Name"]
		industry.save()
		
	return redirect("/")