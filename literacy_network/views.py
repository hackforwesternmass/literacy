from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from datetime import datetime, timedelta
from django.db import DatabaseError
from django.utils import simplejson
from django.contrib.auth.forms import UserCreationForm
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
        user = User.objects.get(id=volunteer.user_id)
    except Volunteer.DoesNotExist:
        print("Volunteer with id {0} does not exist".format(volunteer_id))
        vol_form = VolunteerForm()
        user_form = UserCreationForm()
        user = User()
    except User.DoesNotExist:
        user_form = UserCreationForm()

    if request.method == "POST":
        print("Handling post ...")
        vol_form = VolunteerForm(request.POST, request.FILES, instance=volunteer)
        user_form = UserCreationForm(request.POST, request.FILES, instance=user)

        if vol_form.is_valid() and user_form.is_valid():
            print("Forms valid!")
            svol = vol_form.save()
            user = user_form.save()
            
            return redirect("/volunteers/edit-occupation",  
                        {"volunteer_id" : svol.id})
        else:
            print("Forms not valid!")
            print(vol_form.errors)
            print(user_form.errors)
    elif volunteer_id:
        vol_form = VolunteerForm(instance=volunteer)
        if user:
            user_form = UserCreationForm(instance=user)

    return render(request, 'edit-volunteer.html', 
        {"vol_form" : vol_form, "user_form" : user_form })

@login_required
def volunteers(request):
    """ Presents a list of volunteers """
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers.html',
            {"volunteers" : volunteers})

def upload_industries(request):
    '''Handles upload of industry data in CSV format'''
    if request.method == "POST":
        for row in csv.DictReader(request.FILES["industries-csv"]):
            industry = Industry()
            industry.code=row["Industry_Code"]
            industry.name=row["Industry_Name"]
            industry.save()
	    return redirect("/")
    else:
        return render(request, "upload-industries.html")


		
