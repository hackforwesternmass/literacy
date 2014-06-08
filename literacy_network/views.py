from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from datetime import datetime, timedelta
from django.db import DatabaseError
from django.utils import simplejson
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
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
        vol_form = VolunteerForm()
        user_form = UserCreationForm()
        user = User()
    except User.DoesNotExist:
        user_form = UserCreationForm()

    if request.method == "POST":
        vol_form = VolunteerForm(request.POST, request.FILES, instance=volunteer)
        user_form = UserCreationForm(request.POST, request.FILES, instance=user)

        if vol_form.is_valid() and user_form.is_valid():
            svol = vol_form.save()
            user = user_form.save()

            return redirect("/volunteers/profile/" + str(svol.id)) # shameless hack
    elif volunteer_id:
        vol_form = VolunteerForm(instance=volunteer)
        if user:
            user_form = UserCreationForm(instance=user)

    return render(request, 'edit-volunteer.html', 
        {"vol_form" : vol_form, "user_form" : user_form })

def edit_volunteer_profile(request, volunteer_id):
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)
    data = {}

    # make sure there is a record for each volunteer help type
    new_helps = [q for q in HelpType.objects.all()
                    if not q in [r.help_type for r in 
                             volunteer.helptyperesponse_set.all()]]
    for helptype in new_helps:
        resp = HelpTypeResponse.objects.create(volunteer=volunteer, 
                help_type=helptype, affirmative=False)

    # make sure there is a record for each class site
    new_sites = [s for s in Site.objects.all()
                    if not s in [r.site for r in volunteer.volunteersite_set.all()]]
    for site in new_sites:
        addsite = VolunteerSite.objects.create(volunteer=volunteer, 
                            site=site, affirmative=False)

    if request.method == 'POST':
        occ_formset = OccupationFormset(request.POST, instance=volunteer)
        help_formset = HelpResponseFormset(request.POST, instance=volunteer)
        site_formset = SiteFormset(request.POST, instance=volunteer)

        if occ_formset.is_valid() and help_formset.is_valid() \
                    and site_formset.is_valid():
            occ_formset.save()
            help_formset.save()
            site_formset.save()
    else:
        occ_formset = OccupationFormset(instance=volunteer)
        help_formset = HelpResponseFormset(instance=volunteer)
        site_formset = SiteFormset(instance=volunteer)

    return render(request, 'edit_profile.html', {
        'occ_formset' : occ_formset,
        'help_formset' : help_formset,
        "site_formset" : site_formset
    })

def view_volunteer(request, volunteer_id):
    """ Opens a page for staff members or the public 
        (if the profile is public-enabled) to view a volunteer
    """
    # TODO: check if volunteer is public. if not, and user is not staff, deny request
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)
    return render(request, "view-volunteer.html", {"volunteer" : volunteer})
    

@user_passes_test(lambda u: u.is_staff)
def volunteers(request):
    """ Presents a list of volunteers """
    volunteers = Volunteer.objects.all()
    return render(request, 'volunteers.html',
            {"volunteers" : volunteers})

    return render(request, 'edit-volunteer.html',
        {"form" : form})

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

    return redirect("/")
